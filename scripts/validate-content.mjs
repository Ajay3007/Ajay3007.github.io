#!/usr/bin/env node
/**
 * Content integrity checks that a Zod schema cannot express.
 *
 * The collection schemas in src/content.config.ts validate each entry in
 * isolation — types, enums, required fields. They cannot see across entries,
 * so everything relational is checked here:
 *
 *   1. URL uniqueness            — the Jekyll site silently dropped 3 pages to
 *                                  colliding permalinks and never said a word
 *   2. URL preservation          — none of the 407 live URLs may disappear
 *   3. Reference resolution      — track, module, prerequisites, related,
 *                                  problem_id must point at things that exist
 *   4. Prerequisite cycles       — A requires B requires A
 *   5. Confidentiality gate      — visibility:review must never ship
 *
 * Exits non-zero on any failure, so CI can gate on it.
 *
 *   node scripts/validate-content.mjs
 *   node scripts/validate-content.mjs --production   # also enforces 5
 *   node scripts/validate-content.mjs --require-urls # also enforces 2 fully
 */

import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { join, relative, sep } from 'node:path';
import { parse as parseYaml } from 'yaml';

const ROOT = new URL('..', import.meta.url).pathname;
const CONTENT = join(ROOT, 'src/content');
const INVENTORY = join(ROOT, 'AUDIT_URL_INVENTORY.txt');

const PRODUCTION = process.argv.includes('--production');
const REQUIRE_URLS = process.argv.includes('--require-urls');

const errors = [];
const warnings = [];
const fail = (m) => errors.push(m);
const warn = (m) => warnings.push(m);

/* ── loading ─────────────────────────────────────────────────────────────── */

function walk(dir, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (/\.mdx?$/.test(name)) out.push(p);
  }
  return out;
}

/** Entry id mirrors Astro's: path under the collection, without extension. */
function loadGlob(collection) {
  const base = join(CONTENT, collection);
  return walk(base).map((file) => {
    const raw = readFileSync(file, 'utf8');
    const m = raw.match(/^---\r?\n([\s\S]*?)\r?\n---/);
    if (!m) {
      fail(`${relative(ROOT, file)}: no frontmatter`);
      return null;
    }
    let data;
    try {
      data = parseYaml(m[1]) ?? {};
    } catch (e) {
      fail(`${relative(ROOT, file)}: unparseable frontmatter — ${e.message}`);
      return null;
    }
    const id = relative(base, file).replace(/\.mdx?$/, '').split(sep).join('/');
    return { id, data, file: relative(ROOT, file), collection };
  }).filter(Boolean);
}

function loadJson(name) {
  const p = join(CONTENT, name);
  if (!existsSync(p)) {
    fail(`src/content/${name} is missing`);
    return [];
  }
  try {
    return JSON.parse(readFileSync(p, 'utf8'));
  } catch (e) {
    fail(`src/content/${name}: invalid JSON — ${e.message}`);
    return [];
  }
}

const concepts = loadGlob('concepts');
const tracks = loadGlob('tracks');
const editorials = loadGlob('editorials');
const posts = loadGlob('posts');
const projects = loadGlob('projects');
const modules = loadJson('modules.json');
const problems = loadJson('problems.json');

const addressable = [...concepts, ...tracks, ...editorials, ...posts, ...projects];

/* ── 1. URL uniqueness ───────────────────────────────────────────────────── */

const byUrl = new Map();
for (const e of addressable) {
  const url = e.data.url;
  if (!url) continue;
  if (byUrl.has(url)) {
    fail(`URL collision on ${url}\n     ${byUrl.get(url).file}\n     ${e.file}`);
  } else {
    byUrl.set(url, e);
  }
  for (const r of e.data.redirectFrom ?? []) {
    if (byUrl.has(r)) {
      fail(`redirectFrom ${r} in ${e.file} collides with a real page`);
    }
  }
}

/* ── 1b. URLs differing only by case ─────────────────────────────────────── */

/**
 * Distinct pages on Linux, the same directory on macOS.
 *
 * The Jekyll tree mixes casing (`_learning/dsa/Arrays` next to
 * `_learning/dsa/tree`), and the static files inside those folders are served
 * at the capitalised path while the pages use a lowercased permalink. CI builds
 * on Linux and gets both; a local macOS build silently merges them into
 * whichever directory was created first, which makes local output look like
 * pages have gone missing. Warn rather than fail — the content is legal, it is
 * the local filesystem that cannot represent it.
 */
{
  const byLower = new Map();
  for (const url of byUrl.keys()) {
    const k = url.toLowerCase();
    if (!byLower.has(k)) byLower.set(k, []);
    byLower.get(k).push(url);
  }
  const clashes = [...byLower.values()].filter((v) => v.length > 1);
  for (const set of clashes) warn(`URLs differ only by case: ${set.join('  ')}`);
}

/* ── 2. URL preservation ─────────────────────────────────────────────────── */

let covered = 0;
let live = [];
if (existsSync(INVENTORY)) {
  live = readFileSync(INVENTORY, 'utf8').split('\n').map((s) => s.trim()).filter(Boolean);
  const claimed = new Set(byUrl.keys());
  for (const e of addressable) for (const r of e.data.redirectFrom ?? []) claimed.add(r);
  const missing = live.filter((u) => !claimed.has(u));
  covered = live.length - missing.length;
  if (missing.length && REQUIRE_URLS) {
    fail(`${missing.length} live URL(s) are not served by any entry, e.g.\n     ${missing.slice(0, 5).join('\n     ')}`);
  }
} else {
  warn('AUDIT_URL_INVENTORY.txt not found — URL preservation not checked');
}

/* ── 3. reference resolution ─────────────────────────────────────────────── */

const trackIds = new Set(tracks.map((t) => t.id));
const conceptIds = new Set(concepts.map((c) => c.id));
const problemIds = new Set(problems.map((p) => String(p.id)));
const moduleKeys = new Set(modules.map((m) => `${m.track}/${m.slug}`));

for (const c of concepts) {
  const { track, module: mod, prerequisites = [], related = [] } = c.data;
  if (track && !trackIds.has(track)) fail(`${c.file}: track "${track}" does not exist`);
  if (mod) {
    if (!track) fail(`${c.file}: module "${mod}" set without a track`);
    else if (!moduleKeys.has(`${track}/${mod}`))
      fail(`${c.file}: module "${mod}" is not defined for track "${track}" in modules.json`);
  }
  for (const p of prerequisites)
    if (!conceptIds.has(p)) fail(`${c.file}: prerequisite "${p}" does not resolve to a concept`);
  for (const r of related)
    if (!conceptIds.has(r)) fail(`${c.file}: related "${r}" does not resolve to a concept`);
}

for (const m of modules)
  if (!trackIds.has(m.track)) fail(`modules.json: "${m.id}" references unknown track "${m.track}"`);

for (const e of editorials) {
  const pid = String(e.data.problem_id ?? '');
  if (!problemIds.has(pid))
    fail(`${e.file}: problem_id "${pid}" is not in problems.json`);
}

for (const p of problems)
  for (const c of p.concepts ?? [])
    if (!conceptIds.has(c)) fail(`problems.json: problem ${p.id} references unknown concept "${c}"`);

/* ── 4. prerequisite cycles ──────────────────────────────────────────────── */

{
  const graph = new Map(concepts.map((c) => [c.id, c.data.prerequisites ?? []]));
  const WHITE = 0, GREY = 1, BLACK = 2;
  const colour = new Map([...graph.keys()].map((k) => [k, WHITE]));
  const stack = [];
  const visit = (node) => {
    colour.set(node, GREY);
    stack.push(node);
    for (const next of graph.get(node) ?? []) {
      if (!graph.has(next)) continue;               // already reported in (3)
      if (colour.get(next) === GREY) {
        const cycle = stack.slice(stack.indexOf(next)).concat(next).join(' → ');
        fail(`prerequisite cycle: ${cycle}`);
      } else if (colour.get(next) === WHITE) visit(next);
    }
    stack.pop();
    colour.set(node, BLACK);
  };
  for (const id of graph.keys()) if (colour.get(id) === WHITE) visit(id);
}

/* ── 5. confidentiality gate ─────────────────────────────────────────────── */

const review = addressable.filter((e) => e.data.visibility === 'review');
if (review.length) {
  const list = review.map((e) => `     ${e.file}`).join('\n');
  if (PRODUCTION) fail(`${review.length} entr(y|ies) marked visibility:review must not ship\n${list}`);
  else warn(`${review.length} entr(y|ies) marked visibility:review (blocked from production)\n${list}`);
}

/* ── report ──────────────────────────────────────────────────────────────── */

const counts = [
  ['concepts', concepts.length], ['tracks', tracks.length], ['modules', modules.length],
  ['problems', problems.length], ['editorials', editorials.length],
  ['posts', posts.length], ['projects', projects.length],
];
console.log('content');
for (const [k, v] of counts) console.log(`  ${String(v).padStart(4)}  ${k}`);
if (live.length) {
  const pct = ((covered / live.length) * 100).toFixed(1);
  console.log(`\nURL coverage: ${covered}/${live.length} live URLs served (${pct}%)`);
  if (!REQUIRE_URLS && covered < live.length)
    console.log('  migration in progress — pass --require-urls to make this a failure');
}

if (warnings.length) {
  console.log(`\n${warnings.length} warning(s):`);
  for (const w of warnings) console.log(`  ! ${w}`);
}
if (errors.length) {
  console.log(`\n${errors.length} error(s):`);
  for (const e of errors) console.log(`  ✗ ${e}`);
  console.log('\nFAILED');
  process.exit(1);
}
console.log('\nOK');
