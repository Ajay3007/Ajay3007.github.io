#!/usr/bin/env node
/**
 * Internal link check over the built site.
 *
 * The Jekyll site shipped 17 broken internal links for months because nothing
 * ever looked. This runs after `astro build` and fails on any href that does
 * not resolve to a file in dist/.
 *
 * Only internal links are checked — external URLs are someone else's uptime.
 *
 * Mid-migration, a link can be broken for two very different reasons:
 *   • it points at a URL the live Jekyll site serves and Astro has not built
 *     yet — expected, and shrinks to zero as the phases complete;
 *   • it points at nothing at all — a typo, and a hard failure today.
 * AUDIT_URL_INVENTORY.txt is the discriminator, so the check stays useful from
 * the first day of the migration instead of being switched off until the end.
 *
 *   node scripts/check-links.mjs [dist]
 *   node scripts/check-links.mjs --strict   # pending links fail too (cutover)
 */

import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
const STRICT = process.argv.includes('--strict');
const DIST = join(ROOT, process.argv.find((a) => !a.startsWith('--') && a !== process.argv[0] && a !== process.argv[1]) ?? 'dist');

/** URLs the live Jekyll site serves — broken links to these are "pending". */
const inventoryPath = join(ROOT, 'AUDIT_URL_INVENTORY.txt');
const inventory = new Set(
  existsSync(inventoryPath)
    ? readFileSync(inventoryPath, 'utf8').split('\n').map((s) => s.trim()).filter(Boolean)
    : [],
);

if (!existsSync(DIST)) {
  console.error(`${relative(ROOT, DIST)} does not exist — run the build first.`);
  process.exit(1);
}

function walk(dir, out = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (p.endsWith('.html')) out.push(p);
  }
  return out;
}

/** A link resolves if it maps to a file, a directory index, or a .html sibling. */
function resolves(url) {
  const clean = decodeURI(url.split('#')[0].split('?')[0]);
  const p = join(DIST, clean);
  return existsSync(p) || existsSync(join(p, 'index.html')) || existsSync(`${p.replace(/\/$/, '')}.html`);
}

const pages = walk(DIST);
const broken = new Map(); // url -> Set(pages)
let checked = 0;

for (const page of pages) {
  const html = readFileSync(page, 'utf8');
  for (const m of html.matchAll(/(?:href|src)="(\/[^"]*)"/g)) {
    const url = m[1];
    if (url.startsWith('//')) continue;            // protocol-relative = external
    checked++;
    if (!resolves(url)) {
      if (!broken.has(url)) broken.set(url, new Set());
      broken.get(url).add(relative(DIST, page));
    }
  }
}

console.log(`checked ${checked} internal links across ${pages.length} pages`);

/**
 * Three Jekyll URLs are files rather than directories (/about.html,
 * lambda-functions.html, dsa-mastery-roadmap.html). The audit flagged them as
 * an inconsistency to normalise, so treat a directory URL as pending when the
 * inventory holds its .html twin — the page exists today, at the other spelling,
 * and the move is a redirect rather than a broken link.
 */
const isPending = (url) =>
  inventory.has(url) ||
  inventory.has(url.replace(/\/$/, '') + '.html') ||
  inventory.has(url.replace(/\.html$/, '/'));

const pending = [...broken].filter(([url]) => !STRICT && isPending(url));
const real = [...broken].filter(([url]) => STRICT || !isPending(url));

if (pending.length) {
  console.log(`\n${pending.length} link(s) awaiting migration (served by Jekyll today):`);
  for (const [url] of pending.sort()) console.log(`  · ${url}`);
}

if (real.length) {
  console.log(`\n${real.length} broken target(s):`);
  for (const [url, from] of real.sort()) {
    const list = [...from].slice(0, 3);
    const more = from.size > 3 ? ` (+${from.size - 3} more)` : '';
    console.log(`  ✗ ${url}\n      from: ${list.join(', ')}${more}`);
  }
  console.log('\nFAILED');
  process.exit(1);
}
console.log('\nOK — no broken internal links');
