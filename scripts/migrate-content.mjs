#!/usr/bin/env node
/**
 * One-shot bulk migration of the Jekyll collections into Astro content.
 *
 * Committed rather than run-and-forgotten, so the transform is auditable and
 * re-runnable. It is deliberately conservative:
 *
 *   • Bodies move across UNCHANGED except for Liquid that Astro cannot execute.
 *     Astro renders .md with raw HTML passed through, exactly as kramdown did,
 *     so the 3.18 M characters of embedded markup keep working on day one and
 *     convert to components later, page by page.
 *   • `url` is set to the page's CURRENT permalink, so no live URL moves.
 *   • Anything it cannot infer (status, prerequisites, related) is left unset
 *     rather than guessed. Those are authoring decisions.
 *
 *   node scripts/migrate-content.mjs [--dry]
 */

import { readFileSync, writeFileSync, mkdirSync, existsSync, readdirSync, statSync, rmSync } from 'node:fs';
import { join, dirname, basename, relative } from 'node:path';
import { parse as parseYaml } from 'yaml';

const ROOT = new URL('..', import.meta.url).pathname;
const DRY = process.argv.includes('--dry');
const OUT = join(ROOT, 'src/content');

/* ── taxonomy: old folder → one of the 11 domains ────────────────────────── */
const DOMAIN_OF = {
  'ai-ml': 'ai-ml',
  'data-plane': 'data-plane',
  dsa: 'dsa',
  finance: 'finance',
  networking: 'networking',
  '4g-5g': 'networking',
  'operating-systems': 'systems',
  oop: 'languages',
  'programming-language': 'languages',
  'system-design': 'system-design',
  backend: 'engineering',
  'competitive-programming': 'engineering',
};

/**
 * Track inference. Ordered — first match wins. A page that matches nothing
 * simply has no track, which is valid: `track` is optional.
 */
const TRACKS = [
  [/^_learning\/networking\/networking-mastery\//, 'networking-mastery'],
  [/^_learning\/ai-ml\/part\d/, 'ai-ml-engineering'],
  [/^_learning\/system-design\/lld\//, 'system-design-lld'],
  [/^_learning\/system-design\/hld\//, 'system-design-hld'],
  [/^_learning\/data-plane\/vpp\//, 'vpp'],
  [/^_learning\/data-plane\/dpdk\//, 'dpdk'],
  [/^_learning\/data-plane\/ngfw\//, 'ngfw'],
  [/^_learning\/data-plane\/projects\//, 'dataplane-projects'],
  [/^_learning\/backend\/m\d/, 'backend'],
  [/^_learning\/programming-language\/c\/c-basics\//, 'c-fundamentals'],
  [/^_learning\/dsa\/.*\/ch\d+-/, 'dsa-mastery'],
  [/^_learning\/dsa\/ch\d+-/, 'dsa-mastery'],
];

/**
 * Ordering from the filename, because the Jekyll tree encoded it three
 * incompatible ways. Everything below is read once here and written into
 * `order`, after which the filename stops mattering.
 */
function inferOrder(file) {
  const b = basename(file, '.md');
  let m;
  if ((m = b.match(/^p(\d+)-m(\d+)-/)))  return Number(m[1]) * 100 + Number(m[2]);  // p4-m13-
  if ((m = b.match(/^module-([abc])(\d+)-/i))) {
    const band = { a: 0, b: 100, c: 200 }[m[1].toLowerCase()];
    return band + Number(m[2]) * 2 + (b.includes('-notes') ? 1 : 0);               // module-b9-
  }
  if ((m = b.match(/^m(\d+)-/)))         return Number(m[1]);                       // m17-
  if ((m = b.match(/^ch(\d+)-/)))        return Number(m[1]);                       // ch5-
  if ((m = b.match(/^(\d+)-/)))          return Number(m[1]);                       // 01-
  if ((m = b.match(/^module-p(\d+)-/)))  return Number(m[1]);                       // module-p2-
  if (b === 'index') return 0;
  return 99;
}

/** ai-ml partN-slug folders are already modules; nothing else reliably is. */
function inferModule(file, track) {
  if (track !== 'ai-ml-engineering') return undefined;
  const m = file.match(/^_learning\/ai-ml\/(part\d+-[a-z-]+)\//);
  return m ? m[1] : undefined;
}

/* ── body transforms ─────────────────────────────────────────────────────── */

/**
 * Astro does not run Liquid. `relative_url` is a no-op here because baseurl is
 * empty, so it is unwrapped; anything else is left alone and reported, because
 * silently deleting a template tag would silently delete content.
 */
function convertLiquid(body) {
  const before = body;
  body = body
    /**
     * Jekyll's highlight tag becomes a fenced block — 140 of them. This is a
     * straight upgrade rather than a workaround: Shiki then highlights the code
     * properly, where Jekyll's tag emitted markup the page had to style itself.
     */
    .replace(
      /\{%-?\s*highlight\s+(\w+)[^%]*%\}\r?\n?([\s\S]*?)\r?\n?\{%-?\s*endhighlight\s*-?%\}/g,
      (_m, lang, code) => '```' + lang + '\n' + code.replace(/\s+$/, '') + '\n```',
    )
    /** {% raw %} only existed to stop Jekyll evaluating braces; Astro .md
        never evaluates them, so the wrapper goes and the content stays. */
    .replace(/\{%-?\s*(end)?raw\s*-?%\}\r?\n?/g, '')
    .replace(/\{\{\s*['"]([^'"]+)['"]\s*\|\s*relative_url\s*\}\}/g, '$1')
    .replace(/\{\{\s*['"]([^'"]+)['"]\s*\|\s*absolute_url\s*\}\}/g, '$1')
    .replace(/\{\{\s*site\.baseurl\s*\}\}/g, '');
  const remaining = (body.match(/\{%|\{\{/g) || []).length;
  return { body, changed: body !== before, remaining };
}

/**
 * A raw HTML block ends at the first blank line, per CommonMark — so remark
 * closes a hand-written <pre> there and parses the rest of the code as
 * markdown. kramdown did not, which is why 101 files ship <pre> blocks with
 * blank lines in them (3,640 in total) that rendered fine under Jekyll and
 * come apart under Astro: ASCII diagrams lose their spacing, and a stray
 * `# heading` line inside a template becomes a real <h1>.
 *
 * Replacing those blank lines with a single space keeps the HTML block intact
 * for the parser and is invisible inside a <pre>, where whitespace is
 * preserved anyway. Fenced ``` blocks are untouched — they are already safe.
 */
function sealPreBlocks(body) {
  return body.replace(/<pre[^>]*>[\s\S]*?<\/pre>/g, (block) =>
    block.replace(/\n[ \t]*\n/g, '\n \n'),
  );
}

/**
 * The same CommonMark rule bites outside <pre> too, and harder.
 *
 * A blank line in the middle of a hand-written HTML block closes it. Whatever
 * follows is then read as markdown — and because these blocks are indented,
 * four spaces of indentation turns the next <div> into an *indented code
 * block*, so the raw markup is printed to the page as text. 6,168 blank lines
 * across 174 files sit in exactly that position.
 *
 * A blank line is only removed when the markup clearly continues across it:
 * the previous non-blank line ends a tag and the next opens one. A blank line
 * before real prose is left alone, so the
 *
 *     <div>
 *
 *     **markdown inside a div**
 *
 * idiom keeps working.
 */
function joinHtmlBlocks(body) {
  const lines = body.split('\n');
  const out = [];
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].trim() !== '') { out.push(lines[i]); continue; }

    let p = i - 1;
    while (p >= 0 && lines[p].trim() === '') p--;
    let n = i + 1;
    while (n < lines.length && lines[n].trim() === '') n++;

    const continuesMarkup =
      p >= 0 && n < lines.length &&
      lines[p].trimEnd().endsWith('>') &&
      lines[n].trimStart().startsWith('<');

    if (!continuesMarkup) out.push(lines[i]);
  }
  return out.join('\n');
}

/**
 * Astro resolves relative markdown image paths at build time and hard-fails on
 * a miss, where Jekyll just emitted a broken <img>.
 *
 * Every offender is a placeholder inside a hand-written README/template
 * example (`assets/demo.gif`, `badge-url`) that was never a real file — they
 * only became images because a blank line inside the surrounding raw <pre>
 * ended the HTML block and let the markdown parser back in. They are meant to
 * be read as literal template text, so that is what they become: inline code
 * rather than a permanently broken <img>.
 */
function fixRelativeImages(body, sourceFile) {
  return body.replace(/!\[([^\]]*)\]\(([^)\s]+)([^)]*)\)/g, (m, alt, src, rest) => {
    if (/^(https?:|\/|data:|#)/.test(src)) return m;
    const onDisk = join(ROOT, dirname(sourceFile), src);
    if (existsSync(onDisk)) return m;
    report.placeholderImages.push([sourceFile, src]);
    return `\`![${alt}](${src}${rest})\``;
  });
}

/** First real sentence of prose, for the 354 pages with no description. */
function deriveDescription(body, title) {
  const text = body
    .replace(/<style[\s\S]*?<\/style>/gi, '')
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/```[\s\S]*?```/g, '')
    .replace(/\{%[\s\S]*?%\}/g, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/[#*_>`|]/g, ' ')
    .replace(/&[a-z]+;/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  const sentences = text.split(/(?<=[.!?])\s+/).filter((s) => s.length > 40 && /[a-z]/.test(s));
  let d = sentences[0] ?? '';
  if (d.length > 180) d = d.slice(0, 177).replace(/\s+\S*$/, '') + '…';
  return d || `${title} — notes.`;
}

function quote(s) {
  return `"${String(s).replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`;
}

/* ── inventory: which files migrate, which do not ────────────────────────── */

const inventory = new Map();
for (const line of readFileSync(join(ROOT, 'MIGRATION_INVENTORY.csv'), 'utf8').split('\n').slice(1)) {
  if (!line.trim()) continue;
  const cells = [];
  let cur = '', q = false;
  for (const ch of line) {
    if (ch === '"') q = !q;
    else if (ch === ',' && !q) { cells.push(cur); cur = ''; }
    else cur += ch;
  }
  cells.push(cur);
  inventory.set(cells[0], { status: cells[6], type: cells[1] });
}


/* ── tracks ──────────────────────────────────────────────────────────────── */

/**
 * Every track a concept can reference. `from` names the Jekyll roadmap page
 * that becomes this track's body and donates its URL; tracks without one get a
 * stub and a derived URL, and their landing page is generated in Phase 6.
 */
const TRACK_DEFS = [
  { id: 'dsa-mastery',        domain: 'dsa',           order: 1, from: '_learning/dsa/dsa-roadmap.md',
    title: 'DSA Mastery',            tagline: 'Thirteen chapters, and the problems that prove them.' },
  { id: 'ai-ml-engineering',  domain: 'ai-ml',         order: 1, from: '_learning/ai-ml/ai-ml-roadmap.md',
    title: 'AI & ML Engineering',    tagline: 'Python and statistics through to RAG, agents and MLOps.' },
  { id: 'system-design-hld',  domain: 'system-design', order: 1, from: '_learning/system-design/system-design-roadmap.md',
    title: 'High-Level Design',      tagline: 'Scale, storage, messaging and the case studies that use them.' },
  { id: 'system-design-lld',  domain: 'system-design', order: 2,
    title: 'Low-Level Design',       tagline: 'SOLID, the pattern families, concurrency and case studies.' },
  { id: 'networking-mastery', domain: 'networking',    order: 1, from: '_learning/networking/networking-mastery-roadmap.md',
    title: 'Networking Mastery',     tagline: 'Zero to NGFW, one layer at a time.' },
  { id: 'vpp',                domain: 'data-plane',    order: 1, from: '_learning/data-plane/vpp/vpp-roadmap.md',
    title: 'VPP Internals',          tagline: 'Vector packet processing from vlib up to the host stack.' },
  { id: 'dpdk',               domain: 'data-plane',    order: 2, from: '_learning/data-plane/dpdk/dpdk-roadmap.md',
    title: 'DPDK',                   tagline: 'Poll-mode drivers, mempools and line-rate pipelines.' },
  { id: 'ngfw',               domain: 'data-plane',    order: 3,
    title: 'NGFW Architecture',      tagline: 'How a next-generation firewall is put together.' },
  { id: 'dataplane-projects', domain: 'data-plane',    order: 4, from: '_learning/data-plane/roadmap.md',
    title: 'Data Plane Projects',    tagline: 'Twenty-one build-it-yourself modules, config parser to full pipeline.' },
  { id: 'backend',            domain: 'engineering',   order: 1, from: '_learning/backend/backend-roadmap.md',
    title: 'Backend Engineering',    tagline: 'HTTP fundamentals to production-hardened systems.' },
  { id: 'c-fundamentals',     domain: 'languages',     order: 1,
    title: 'C Fundamentals',         tagline: 'Memory, pointers, structs and what the compiler actually does.' },
];

function writeTracks() {
  const bySource = new Map(TRACK_DEFS.filter((t) => t.from).map((t) => [t.from, t]));
  for (const def of TRACK_DEFS) {
    let body = '';
    let url;
    let trackHead = '';
    let trackFoot = '';
    let description = def.tagline;

    if (def.from && existsSync(join(ROOT, def.from))) {
      const raw = readFileSync(join(ROOT, def.from), 'utf8');
      const fm = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
      if (fm) {
        const data = parseYaml(fm[1]) ?? {};
        url = data.permalink;
        if (data.custom_css) trackHead = `<link rel="stylesheet" href="/assets/css/${data.custom_css}.css">`;
        if (data.custom_js) trackFoot = `<script src="/assets/js/${data.custom_js}.js" defer></script>`;
        const converted = convertLiquid(fm[2]);
        body = joinHtmlBlocks(sealPreBlocks(converted.body));
        if (converted.remaining) report.liquidLeft.push([def.from, converted.remaining]);
        description = data.description ?? deriveDescription(body, def.title);
      }
    }

    const out = ['---'];
    out.push(`title: ${quote(def.title)}`);
    out.push(`tagline: ${quote(def.tagline)}`);
    out.push(`description: ${quote(description)}`);
    out.push(`domain: ${def.domain}`);
    out.push(`order: ${def.order}`);
    out.push('status: active');
    if (url) out.push(`url: ${url}`);
    out.push('---', '');
    if (trackHead) out.push(trackHead, '');
    out.push(body.replace(/^\n+/, ''));
    if (trackFoot) out.push('', trackFoot);

    const dest = join(OUT, 'tracks', `${def.id}.md`);
    if (!DRY) { mkdirSync(dirname(dest), { recursive: true }); writeFileSync(dest, out.join('\n')); }
    report.tracks.push([def.id, url ?? '(derived)', def.from ?? '(stub)']);
  }

  // Roadmap pages that are not a track's body still need reporting.
  for (const f of roadmapFiles) if (!bySource.has(f)) report.skipped.push([f, 'CONVERT-UNMAPPED', '']);
}

/* ── run ─────────────────────────────────────────────────────────────────── */

function walk(dir, out = []) {
  for (const n of readdirSync(dir)) {
    const p = join(dir, n);
    if (statSync(p).isDirectory()) { if (n !== 'manim-scripts') walk(p, out); }
    else if (p.endsWith('.md')) out.push(relative(ROOT, p));
  }
  return out;
}

/** Domains that more than one Jekyll folder maps into. */
const MERGED_DOMAINS = new Set(
  Object.entries(
    Object.entries(DOMAIN_OF).reduce((acc, [folder, d]) => {
      (acc[d] ??= []).push(folder);
      return acc;
    }, {}),
  )
    .filter(([, folders]) => folders.length > 1)
    .map(([d]) => d),
);

/** Guards against two sources writing to one destination. */
const written = new Map();

const report = { migrated: [], skipped: [], autoDescription: [], liquidLeft: [], noTrack: [], tracks: [], placeholderImages: [] };
const roadmapFiles = [];
const modulesSeen = new Map();

for (const file of walk(join(ROOT, '_learning')).sort()) {
  const inv = inventory.get(file);
  const status = inv?.status ?? 'MIGRATE';
  const type = inv?.type ?? '';

  // Roadmap pages become tracks, handled separately below.
  if (status === 'CONVERT') { roadmapFiles.push(file); continue; }

  /**
   * Section index.md pages were marked REVIEW because most of their content is
   * derivable. They are still live URLs, so they migrate now and get replaced
   * by generated indexes page by page — skipping them would 404.
   */
  const migrateAnyway = status === 'REVIEW' && type === 'Section index';
  if (status !== 'MIGRATE' && !migrateAnyway) {
    report.skipped.push([file, status, type]);
    continue;
  }

  const raw = readFileSync(join(ROOT, file), 'utf8');
  const fm = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!fm) { report.skipped.push([file, 'NO-FRONTMATTER', '']); continue; }

  const data = parseYaml(fm[1]) ?? {};
  if (data.published === false) { report.skipped.push([file, 'UNPUBLISHED', '']); continue; }

  const segs = file.split('/');
  const domain = DOMAIN_OF[segs[1]];
  if (!domain) { report.skipped.push([file, 'NO-DOMAIN-MAPPING', segs[1]]); continue; }

  const track = TRACKS.find(([re]) => re.test(file))?.[1];
  const module = inferModule(file, track);
  if (module) modulesSeen.set(`${track}/${module}`, { track, slug: module });
  if (!track) report.noTrack.push(file);

  const url = data.permalink ?? '/' + file.replace(/^_/, '').replace(/\/index\.md$/, '/').replace(/\.md$/, '/');
  const { body: liquidFixed, remaining } = convertLiquid(fm[2]);
  const body = joinHtmlBlocks(sealPreBlocks(fixRelativeImages(liquidFixed, file)));
  if (remaining) report.liquidLeft.push([file, remaining]);

  let description = data.description;
  if (!description) {
    description = deriveDescription(body, data.title ?? basename(file, '.md'));
    report.autoDescription.push(file);
  }

  /**
   * The Jekyll layout injected per-page CSS/JS from `custom_css` / `custom_js`
   * front matter. Astro has no equivalent hook, and 41 pages depend on it, so
   * the tags move into the body — which is exactly how the other 15 bespoke
   * pages already did it. sync-public.mjs puts the files where these point.
   */
  const headTags = [];
  if (data.custom_css) headTags.push(`<link rel="stylesheet" href="/assets/css/${data.custom_css}.css">`);
  const footTags = [];
  if (data.custom_js) footTags.push(`<script src="/assets/js/${data.custom_js}.js" defer></script>`);

  const out = ['---'];
  out.push(`title: ${quote(data.title ?? basename(file, '.md'))}`);
  out.push(`description: ${quote(description)}`);
  out.push(`domain: ${domain}`);
  if (track) out.push(`track: ${track}`);
  if (module) out.push(`module: ${module}`);
  out.push(`order: ${inferOrder(file)}`);
  // Jekyll's `layout: default` meant "this page draws its own everything".
  if (data.layout === 'default') out.push('chrome: bare');
  if (/<h1[\s>]|^\s*#\s+\S|class="[^"]*(hdr|header|hero)/im.test(body)) out.push('ownHeader: true');
  out.push(`url: ${url}`);
  out.push('---', '');
  if (headTags.length) out.push(...headTags, '');
  out.push(body.replace(/^\n+/, ''));
  if (footTags.length) out.push('', ...footTags);

  /**
   * _learning/networking/networking-mastery/m05-tcp.md
   *   -> concepts/networking/networking-mastery/m05-tcp.md
   *
   * Where several old folders fold into one domain (4g-5g + networking, oop +
   * programming-language, backend + competitive-programming) the source folder
   * is kept in the path, otherwise both index.md files land on the same
   * destination and one silently overwrites the other.
   */
  const sub = (MERGED_DOMAINS.has(domain) ? segs.slice(1) : segs.slice(2)).join('/');
  const dest = join(OUT, 'concepts', domain, sub);

  if (written.has(dest)) {
    throw new Error(
      `destination collision: ${relative(ROOT, dest)}\n  <- ${written.get(dest)}\n  <- ${file}`,
    );
  }
  written.set(dest, file);
  if (!DRY) { mkdirSync(dirname(dest), { recursive: true }); writeFileSync(dest, out.join('\n')); }
  report.migrated.push([file, relative(ROOT, dest), url]);
}

writeTracks();

// Modules discovered from the ai-ml part folders, plus the networking seeds.
if (!DRY) {
  const existing = existsSync(join(OUT, 'modules.json'))
    ? JSON.parse(readFileSync(join(OUT, 'modules.json'), 'utf8'))
    : [];
  const seen = new Set(existing.map((m) => m.id));
  const titleOf = (slug) =>
    slug.replace(/^part\d+-/, '').replace(/-/g, ' ').replace(/^./, (c) => c.toUpperCase());
  for (const [id, { track, slug }] of modulesSeen) {
    if (seen.has(id)) continue;
    existing.push({
      id, track, slug,
      title: titleOf(slug),
      description: `${titleOf(slug)} — part of the ${track} track.`,
      order: Number(slug.match(/^part(\d+)/)?.[1] ?? 99),
    });
  }
  existing.sort((a, b) => a.track.localeCompare(b.track) || a.order - b.order);
  writeFileSync(join(OUT, 'modules.json'), JSON.stringify(existing, null, 2) + '\n');
}

/* ── report ──────────────────────────────────────────────────────────────── */
const pad = (n) => String(n).padStart(4);
console.log(DRY ? 'DRY RUN — nothing written\n' : '');
console.log(`${pad(report.migrated.length)}  migrated`);
console.log(`${pad(report.skipped.length)}  skipped`);
console.log(`${pad(report.autoDescription.length)}  descriptions auto-derived (review these)`);
console.log(`${pad(report.liquidLeft.length)}  files still containing Liquid (manual)`);
console.log(`${pad(report.noTrack.length)}  migrated without a track`);
console.log(`${pad(modulesSeen.size)}  modules discovered`);
console.log(`${pad(report.tracks.length)}  tracks written`);
console.log(`${pad(report.placeholderImages.length)}  placeholder image paths kept as literal text`);

const bySkip = {};
for (const [, s] of report.skipped) bySkip[s] = (bySkip[s] ?? 0) + 1;
console.log('\nskipped by reason:');
for (const [k, v] of Object.entries(bySkip).sort((a, b) => b[1] - a[1])) console.log(`  ${pad(v)}  ${k}`);

if (report.liquidLeft.length) {
  console.log('\nLiquid needing manual conversion:');
  for (const [f, n] of report.liquidLeft) console.log(`  ${pad(n)}  ${f}`);
}

if (!DRY) {
  writeFileSync(join(ROOT, 'MIGRATION_REPORT.md'), [
    '# Migration report', '',
    `Generated by \`scripts/migrate-content.mjs\`.`, '',
    `- migrated: ${report.migrated.length}`,
    `- skipped: ${report.skipped.length}`,
    `- auto-derived descriptions: ${report.autoDescription.length}`,
    `- files still containing Liquid: ${report.liquidLeft.length}`,
    `- migrated without a track: ${report.noTrack.length}`, '',
    '## Descriptions to review', '',
    'These had no `description` in Jekyll. One was derived from the first',
    'sentence of the body so the page has a real meta description today; each',
    'is worth a human pass.', '',
    ...report.autoDescription.map((f) => `- \`${f}\``), '',
    '## Skipped', '',
    '| file | reason |', '|---|---|',
    ...report.skipped.map(([f, s]) => `| \`${f}\` | ${s} |`), '',
  ].join('\n'));
  console.log('\nwrote MIGRATION_REPORT.md');
}
