#!/usr/bin/env node
/**
 * Bulk migration of the smaller Jekyll collections: _posts, _projects and
 * _editorials. Companion to migrate-content.mjs, which handles _learning.
 *
 * Same rules: bodies move across unchanged apart from Liquid Astro cannot run,
 * URLs are carried from the existing permalink so nothing moves, and anything
 * that cannot be inferred is left unset rather than guessed.
 *
 *   node scripts/migrate-collections.mjs
 */
import { readFileSync, writeFileSync, mkdirSync, readdirSync, statSync } from 'node:fs';
import { join, dirname, basename, relative } from 'node:path';
import { parse as parseYaml } from 'yaml';
const ROOT = new URL('..', import.meta.url).pathname, OUT = join(ROOT, 'src/content');
const q = (s) => `"${String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"')}"`;
const liq = (b) => b.replace(/\{\{\s*['"]([^'"]+)['"]\s*\|\s*relative_url\s*\}\}/g,'$1')
                    .replace(/\{\{\s*site\.baseurl\s*\}\}/g,'');
const desc = (body, title) => {
  const t = body.replace(/<style[\s\S]*?<\/style>/gi,'').replace(/<script[\s\S]*?<\/script>/gi,'')
    .replace(/```[\s\S]*?```/g,'').replace(/<[^>]+>/g,' ').replace(/[#*_>`|]/g,' ')
    .replace(/&[a-z]+;/gi,' ').replace(/\s+/g,' ').trim();
  const s = t.split(/(?<=[.!?])\s+/).filter(x => x.length > 40 && /[a-z]/.test(x))[0] ?? '';
  return (s.length > 180 ? s.slice(0,177).replace(/\s+\S*$/,'')+'…' : s) || `${title}.`;
};
const walk = (d, o=[]) => { for (const n of readdirSync(d)) { const p=join(d,n);
  statSync(p).isDirectory() ? walk(p,o) : p.endsWith('.md') && o.push(p); } return o; };

let counts = {};
// ── posts ────────────────────────────────────────────────────────────────
for (const f of walk(join(ROOT,'_posts'))) {
  const raw = readFileSync(f,'utf8');
  const m = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/); if(!m) continue;
  const d = parseYaml(m[1]) ?? {}, body = liq(m[2]);
  const b = basename(f,'.md'), dm = b.match(/^(\d{4})-(\d{2})-(\d{2})-(.+)$/);
  const url = `/blog/${dm[1]}/${dm[2]}/${dm[3]}/${dm[4]}/`;
  const out = ['---', `title: ${q(d.title)}`,
    `description: ${q(d.excerpt ?? desc(body, d.title))}`,
    `date: ${dm[1]}-${dm[2]}-${dm[3]}`];
  const cats = [].concat(d.categories ?? []);
  if (cats.length) out.push(`tags: [${cats.join(', ')}]`);
  out.push(`url: ${url}`, '---', '', body.replace(/^\n+/,''));
  const dest = join(OUT,'posts',`${dm[4]}.md`);
  mkdirSync(dirname(dest),{recursive:true}); writeFileSync(dest,out.join('\n'));
  counts.posts = (counts.posts??0)+1;
}
// ── projects ─────────────────────────────────────────────────────────────
for (const f of walk(join(ROOT,'_projects'))) {
  const raw = readFileSync(f,'utf8');
  const m = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/); if(!m) continue;
  const d = parseYaml(m[1]) ?? {}, body = liq(m[2]);
  const out = ['---', `title: ${q(d.title)}`,
    `description: ${q(d.description ?? desc(body, d.title))}`,
    `year: ${d.year ?? new Date().getFullYear()}`];
  if (d.tags?.length) out.push(`tech: [${d.tags.map(t=>q(t)).join(', ')}]`);
  if (d.github) out.push(`github: ${d.github}`);
  if (d.demo) out.push(`demo: ${d.demo}`);
  out.push(`url: ${d.permalink ?? `/projects/${basename(f,'.md')}/`}`, '---','', body.replace(/^\n+/,''));
  const dest = join(OUT,'projects',basename(f));
  mkdirSync(dirname(dest),{recursive:true}); writeFileSync(dest,out.join('\n'));
  counts.projects = (counts.projects??0)+1;
}
// ── editorials ───────────────────────────────────────────────────────────
for (const f of walk(join(ROOT,'_editorials'))) {
  const raw = readFileSync(f,'utf8');
  const m = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/); if(!m) continue;
  const d = parseYaml(m[1]) ?? {}, body = liq(m[2]);
  const date = d.date instanceof Date ? d.date.toISOString().slice(0,10) : String(d.date).slice(0,10);
  const out = ['---', `title: ${q(d.title)}`,
    `description: ${q(desc(body, d.title))}`,
    `problem_id: ${q(String(d.problem_id ?? ''))}`,
    `date: ${date}`,
    `url: ${d.permalink ?? `/editorials/${basename(f,'.md')}/`}`, '---','', body.replace(/^\n+/,'')];
  const dest = join(OUT,'editorials',basename(f));
  mkdirSync(dirname(dest),{recursive:true}); writeFileSync(dest,out.join('\n'));
  counts.editorials = (counts.editorials??0)+1;
}
console.log(counts);
