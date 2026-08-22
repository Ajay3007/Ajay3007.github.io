/**
 * Single source of truth for identity, navigation and taxonomy.
 *
 * Every component reads from here, so there is exactly one place to edit when
 * something changes. In particular: adding a knowledge domain is one entry in
 * DOMAINS below, and nothing else — the schemas validate against it, the
 * indexes group by it, and search filters by it.
 */

export const SITE = {
  url: 'https://ajay3007.github.io',
  title: 'ajdevhub',
  tagline: 'Notes, projects and roadmaps from five years in the data plane.',
  description:
    'Engineering knowledge platform of Ajay Kumar Gupt — data plane, networking, systems, ' +
    'compilers and AI. Learning notes, DSA problems, project write-ups and roadmaps.',
  author: 'Ajay Kumar Gupt',
  locale: 'en_IN',
  lang: 'en',
  ogImage: '/assets/images/og-default.png',
} as const;

export const PROFILE = {
  name: 'Ajay Kumar Gupt',
  role: 'Software Engineer',
  company: 'Jio Platforms',
  location: 'Navi Mumbai',
  github: 'Ajay3007',
  linkedin: 'ajay-gupt',
  /** Rolling "what I'm on right now" line, surfaced on the home hero. */
  currentFocus:
    'Working through transformers and graph compilers — computational graphs, IR, ' +
    'graph optimisation and how any of it reaches hardware.',
} as const;

export const SOCIALS = [
  { label: 'GitHub', href: `https://github.com/${PROFILE.github}`, icon: 'github' },
  { label: 'LinkedIn', href: `https://linkedin.com/in/${PROFILE.linkedin}`, icon: 'linkedin' },
] as const;

/**
 * Knowledge domains — the top level of Domain → Track → Module → Concept.
 *
 * `domain` is metadata, never a URL segment: URLs are carried explicitly on
 * each concept so the 401 existing URLs survive regrouping untouched. That
 * means this list can be reorganised later without breaking a single link.
 */
export const DOMAINS = [
  { slug: 'data-plane', label: 'Data Plane', group: 'Systems', blurb: 'DPDK, VPP, line-rate packet processing' },
  { slug: 'networking', label: 'Networking', group: 'Systems', blurb: 'TCP/IP, routing, TLS, 4G/5G, NGFW' },
  { slug: 'systems', label: 'Systems & OS', group: 'Systems', blurb: 'Memory, scheduling, processes, IPC' },
  { slug: 'distributed', label: 'Distributed Systems', group: 'Systems', blurb: 'Consensus, replication, partitioning' },

  { slug: 'dsa', label: 'DSA & Algorithms', group: 'Foundations', blurb: 'Patterns, structures, complexity' },
  { slug: 'system-design', label: 'System Design', group: 'Foundations', blurb: 'HLD, LLD, scale and trade-offs' },
  { slug: 'languages', label: 'Programming Languages', group: 'Foundations', blurb: 'C, C++, Java, Python, OOP and design patterns' },

  { slug: 'ai-ml', label: 'AI / ML', group: 'Applied', blurb: 'Foundations, neural networks, transformers, LLMs' },
  { slug: 'compilers', label: 'Compilers & Graph Compilers', group: 'Applied', blurb: 'Computational graphs, IR, optimisation, codegen' },
  { slug: 'engineering', label: 'Engineering Practice', group: 'Applied', blurb: 'Backend, tooling, workflow, competitive programming' },
  { slug: 'finance', label: 'Finance', group: 'Applied', blurb: 'Markets, taxation, personal finance engineering' },
] as const;

/**
 * Sidebar grouping, derived from DOMAINS rather than listed separately —
 * Jekyll kept the same three groups in _data/nav.yml as a second copy that had
 * to be edited alongside the folder tree. Order follows DOMAINS.
 */
export const DOMAIN_GROUPS = [...new Set(DOMAINS.map((d) => d.group))].map((group) => ({
  group,
  domains: DOMAINS.filter((d) => d.group === group),
}));

export type DomainSlug = (typeof DOMAINS)[number]['slug'];

export const DOMAIN_LABELS: Record<string, string> = Object.fromEntries(
  DOMAINS.map((d) => [d.slug, d.label]),
);

/**
 * Authored learning status — the author's own claim about a concept, honest
 * rather than aspirational. Optional on every page: absent means "no claim",
 * which is different from "not started".
 */
export const STATUSES = [
  { slug: 'not-started', label: 'Not started', glyph: '○' },
  { slug: 'learning', label: 'Learning', glyph: '◐' },
  { slug: 'understood', label: 'Understood', glyph: '◕' },
  { slug: 'solid', label: 'Solid', glyph: '●' },
] as const;

export type StatusSlug = (typeof STATUSES)[number]['slug'];

export const STATUS_LABELS: Record<string, string> = Object.fromEntries(
  STATUSES.map((s) => [s.slug, s.label]),
);

/** Top navigation. Kept short deliberately — the header must never wrap. */
export const NAV = [
  { label: 'Learning', href: '/learning/' },
  { label: 'Problems', href: '/problems/' },
  { label: 'Roadmaps', href: '/roadmap/' },
  { label: 'Projects', href: '/projects/' },
  { label: 'Blog', href: '/blogs/' },
  { label: 'About', href: '/about/' },
] as const;

/** Flat list for the command palette and the footer sitemap. */
export const ALL_PAGES = [
  { label: 'Home', href: '/', section: 'Pages' },
  { label: 'Learning', href: '/learning/', section: 'Pages' },
  { label: 'Problems Hub', href: '/problems/', section: 'Pages' },
  { label: 'Roadmaps', href: '/roadmap/', section: 'Pages' },
  { label: 'Projects', href: '/projects/', section: 'Pages' },
  { label: 'Blog archive', href: '/blogs/', section: 'Pages' },
  { label: 'About', href: '/about/', section: 'Pages' },
] as const;
