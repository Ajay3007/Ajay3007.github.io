import type { APIRoute } from 'astro';
import { ALL_PAGES, DOMAINS, DOMAIN_LABELS } from '../consts';
import { getConcepts, getTracks, trackUrl } from '../lib/content';
import { TOPIC_PAGES } from '../lib/problems';

/**
 * The navigation half of search: "take me to X".
 *
 * Titles and destinations only — Pagefind handles full text. Emitted as a
 * static file the palette fetches on first open, so a visitor who never
 * searches never downloads it.
 */
export const GET: APIRoute = async () => {
  const [concepts, tracks] = await Promise.all([getConcepts(), getTracks()]);

  const index = [
    ...ALL_PAGES.map((p) => ({ title: p.label, href: p.href, section: 'Pages' })),

    ...DOMAINS.filter((d) => concepts.some((c) => c.data.domain === d.slug)).map((d) => ({
      title: DOMAIN_LABELS[d.slug]!,
      href: `/learning/${d.slug}/`,
      section: 'Domain',
    })),

    ...tracks.map((t) => ({ title: t.data.title, href: trackUrl(t), section: 'Track' })),

    ...TOPIC_PAGES.map((t) => ({
      title: `${t.title} problems`,
      href: t.url,
      section: 'Problems',
    })),
  ];

  return new Response(JSON.stringify(index), {
    headers: { 'Content-Type': 'application/json' },
  });
};
