#!/usr/bin/env node
/**
 * Mirrors the Jekyll static tree into public/ so migrated pages keep working.
 *
 * The 57 bespoke pages still link their own stylesheet and script, and the
 * whole corpus links diagrams, PDFs and code samples that Jekyll served
 * straight out of the collection folders. Rather than commit a second copy of
 * ~6 MB, this runs as a prebuild step and the mirrored paths are gitignored:
 * the Jekyll tree stays the single source of truth for the whole migration.
 *
 * At the Phase 11 cutover these assets move into public/ for real and this
 * script goes away.
 *
 *   node scripts/sync-public.mjs
 */

import { cpSync, mkdirSync, rmSync, existsSync, readdirSync, statSync } from 'node:fs';
import { join, dirname, relative, extname } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
const PUBLIC = join(ROOT, 'public');

/** Whole directories mirrored as-is. */
const DIRS = [
  ['assets', 'assets'],
  ['images', 'images'],
];

/** Extensions inside _learning that Jekyll served as static files. */
const STATIC_EXT = new Set(['.pdf', '.cpp', '.c', '.h', '.sh', '.puml', '.docx', '.csv', '.png', '.jpg', '.svg', '.gif']);

let dirCount = 0;
for (const [from, to] of DIRS) {
  const src = join(ROOT, from);
  if (!existsSync(src)) continue;
  const dest = join(PUBLIC, to);
  rmSync(dest, { recursive: true, force: true });
  cpSync(src, dest, { recursive: true });
  dirCount++;
}

function walk(dir, out = []) {
  for (const n of readdirSync(dir)) {
    const p = join(dir, n);
    if (statSync(p).isDirectory()) { if (n !== 'manim-scripts') walk(p, out); }
    else out.push(p);
  }
  return out;
}

let fileCount = 0;
const learning = join(ROOT, '_learning');
if (existsSync(learning)) {
  rmSync(join(PUBLIC, 'learning'), { recursive: true, force: true });
  for (const src of walk(learning)) {
    if (!STATIC_EXT.has(extname(src).toLowerCase())) continue;
    // Jekyll served these at /learning/<path-below-_learning>, case intact.
    const dest = join(PUBLIC, 'learning', relative(learning, src));
    mkdirSync(dirname(dest), { recursive: true });
    cpSync(src, dest);
    fileCount++;
  }
}

console.log(`synced ${dirCount} director(ies) and ${fileCount} static file(s) into public/`);
