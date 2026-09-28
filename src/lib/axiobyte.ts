/**
 * The AxioByte experiences manifest — what /axiobyte/ and its domain pages list.
 *
 * It arrives with the pinned release (scripts/fetch-axiobyte.mjs mounts it at
 * public/axiobyte/manifest.json before the build), so the hub always lists
 * exactly the interactive pages that are actually being served.
 */
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

export interface Experience {
  /** Relative to /axiobyte/, e.g. `networking/nic/`. */
  path: string;
  domain: string;
  concept: string;
  title: string;
  summary: string;
  tags?: string[];
  /** The Studio episode this is the interactive side of. */
  episode?: string;
  /** Where the video lives, once published. */
  video?: string;
  /** A /learning/ page that explains the concept in prose. */
  docs?: string;
}

export interface Domain {
  id: string;
  title: string;
  summary: string;
  experiences: Experience[];
}

export interface Manifest {
  version: string;
  domains: Domain[];
}

export function axiobyteManifest(): Manifest {
  const file = join(process.cwd(), 'public', 'axiobyte', 'manifest.json');
  if (!existsSync(file)) {
    throw new Error(
      'public/axiobyte/manifest.json is missing. Run `npm run axiobyte` first ' +
        '(or AXIOBYTE_LOCAL=<experiences dist> npm run axiobyte for a local build).',
    );
  }
  return JSON.parse(readFileSync(file, 'utf8')) as Manifest;
}

export const experienceUrl = (e: Experience) => `/axiobyte/${e.path}`;
