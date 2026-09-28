#!/usr/bin/env node
/**
 * Mount the AxioByte interactive experiences at public/axiobyte/, so the build
 * serves them at /axiobyte/<domain>/<concept>/ (e.g. /axiobyte/networking/nic/).
 *
 * The source lives in github.com/Ajay3007/axiobyte-studio; this site only pins a
 * released build of it in axiobyte.json. Nothing fetched here is committed
 * (public/axiobyte/ is gitignored), so the site never becomes a second copy of
 * the engine.
 *
 *   node scripts/fetch-axiobyte.mjs                 the pinned release (CI does this)
 *   AXIOBYTE_LOCAL=../axiobyte-studio/experiences/dist node scripts/fetch-axiobyte.mjs
 *                                                   a local build, for working on both at once
 *
 * The release is verified against the pinned sha256 before anything is written.
 */
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { cpSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const MOUNT = join(ROOT, 'public', 'axiobyte');
const pin = JSON.parse(readFileSync(join(ROOT, 'axiobyte.json'), 'utf8'));

function fail(message, fix) {
  console.error(`fetch-axiobyte: ${message}${fix ? `\n  fix: ${fix}` : ''}`);
  process.exit(1);
}

function mount(from) {
  if (!existsSync(join(from, 'manifest.json'))) fail(`${from} has no manifest.json — is it an experiences build?`);
  rmSync(MOUNT, { recursive: true, force: true });
  mkdirSync(MOUNT, { recursive: true });
  cpSync(from, MOUNT, { recursive: true });
  const manifest = JSON.parse(readFileSync(join(MOUNT, 'manifest.json'), 'utf8'));
  const pages = manifest.domains.flatMap((d) => d.experiences.map((e) => `/axiobyte/${e.path}`));
  console.log(`mounted AxioByte experiences ${manifest.version} → public/axiobyte/`);
  pages.forEach((p) => console.log(`  ${p}`));
}

const local = process.env.AXIOBYTE_LOCAL;
if (local) {
  mount(resolve(local));
  process.exit(0);
}

if (!pin.sha256) {
  fail(
    `axiobyte.json pins ${pin.tag} without a sha256`,
    `publish the release from axiobyte-studio (tag ${pin.tag}), then copy the hash from ${pin.asset}.sha256 into axiobyte.json`,
  );
}

const url = `https://github.com/${pin.repo}/releases/download/${pin.tag}/${pin.asset}`;
const response = await fetch(url);
if (!response.ok) fail(`GET ${url} → ${response.status}`, `check that release ${pin.tag} exists and has ${pin.asset}`);
const bytes = Buffer.from(await response.arrayBuffer());
const actual = createHash('sha256').update(bytes).digest('hex');
if (actual !== pin.sha256) {
  fail(`${pin.asset} does not match the pinned sha256 (got ${actual.slice(0, 16)}…)`, 'a release asset must never change; pin the new tag instead');
}

const work = mkdtempSync(join(tmpdir(), 'axiobyte-'));
try {
  const archive = join(work, pin.asset);
  writeFileSync(archive, bytes);
  const extracted = join(work, 'dist');
  mkdirSync(extracted);
  execFileSync('tar', ['-xzf', archive, '-C', extracted], { stdio: 'inherit' });
  mount(extracted);
} finally {
  rmSync(work, { recursive: true, force: true });
}
