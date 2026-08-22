import { getCollection, type CollectionEntry } from 'astro:content';

/**
 * Build-time queries. Everything here runs during the build; nothing ships.
 *
 * The one thing deliberately NOT here is visitor completion state — that is
 * per-browser, lives in localStorage, and is applied on the client. Keeping
 * the two apart is what lets pages be fully static and still show progress.
 */

export type Concept = CollectionEntry<'concepts'>;
export type Track = CollectionEntry<'tracks'>;

/** Drafts and review-gated pages never reach a production build. */
export const isPublished = (e: { data: { draft?: boolean; visibility?: string } }) =>
  !e.data.draft && e.data.visibility !== 'review';

/** A concept's URL: the carried one, else derived from domain and slug. */
export function conceptUrl(c: Concept): string {
  if (c.data.url) return c.data.url;
  const slug = c.id.split('/').pop();
  return `/learning/${c.data.domain}/${slug}/`;
}

export function trackUrl(t: Track): string {
  return t.data.url ?? `/learning/${t.id}/`;
}

export async function getConcepts(filter?: { domain?: string; track?: string }) {
  const all = await getCollection('concepts', isPublished);
  return all
    .filter((c) => !filter?.domain || c.data.domain === filter.domain)
    .filter((c) => !filter?.track || c.data.track === filter.track)
    .sort((a, b) => a.data.order - b.data.order || a.data.title.localeCompare(b.data.title));
}

export async function getTracks(domain?: string) {
  const all = await getCollection('tracks', isPublished);
  return all
    .filter((t) => !domain || t.data.domain === domain)
    .sort((a, b) => a.data.order - b.data.order);
}

/* ── the knowledge graph (brief §11) ─────────────────────────────────────── */

export interface Neighbourhood {
  prerequisites: Concept[];
  related: Concept[];
  /** Concepts that name THIS one — derived, never authored twice. */
  backlinks: Concept[];
}

/**
 * Resolves a concept's relationships in both directions.
 *
 * Backlinks are derived: a relationship is declared once, on one side, and
 * shows up on both. Unresolvable ids cannot reach here — validate-content.mjs
 * fails the build on them — so the lookups below are total.
 */
export async function getNeighbourhood(concept: Concept): Promise<Neighbourhood> {
  const all = await getConcepts();
  const byId = new Map(all.map((c) => [c.id, c]));
  const pick = (ids: string[]) => ids.map((id) => byId.get(id)).filter((c): c is Concept => !!c);

  const named = new Set([...concept.data.prerequisites, ...concept.data.related]);
  const backlinks = all.filter(
    (c) =>
      c.id !== concept.id &&
      !named.has(c.id) &&
      [...c.data.prerequisites, ...c.data.related].includes(concept.id),
  );

  return {
    prerequisites: pick(concept.data.prerequisites),
    related: pick(concept.data.related),
    backlinks,
  };
}

/**
 * Previous/next across a whole track, crossing module boundaries — the reader
 * experiences one continuous sequence, not disconnected units.
 */
export async function getNeighbours(concept: Concept) {
  if (!concept.data.track) return { previous: null, next: null };
  const ordered = await getConcepts({ track: concept.data.track });
  const i = ordered.findIndex((c) => c.id === concept.id);
  return {
    previous: i > 0 ? ordered[i - 1]! : null,
    next: i >= 0 && i < ordered.length - 1 ? ordered[i + 1]! : null,
  };
}

export function formatDuration(minutes?: number): string | null {
  if (!minutes) return null;
  if (minutes < 60) return `${minutes} min`;
  const h = Math.floor(minutes / 60);
  const m = minutes % 60;
  return m ? `${h}h ${m}m` : `${h}h`;
}
