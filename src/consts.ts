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
  { slug: 'ai-ml', label: 'AI / ML', blurb: 'Foundations, neural networks, transformers, LLMs' },
  { slug: 'compilers', label: 'Compilers & Graph Compilers', blurb: 'Computational graphs, IR, optimisation, codegen' },
  { slug: 'systems', label: 'Systems & OS', blurb: 'Memory, scheduling, processes, IPC' },
  { slug: 'networking', label: 'Networking', blurb: 'TCP/IP, routing, TLS, 4G/5G, NGFW' },
  { slug: 'data-plane', label: 'Data Plane', blurb: 'DPDK, VPP, line-rate packet processing' },
  { slug: 'distributed', label: 'Distributed Systems', blurb: 'Consensus, replication, partitioning' },
  { slug: 'system-design', label: 'System Design', blurb: 'HLD, LLD, scale and trade-offs' },
  { slug: 'dsa', label: 'DSA & Algorithms', blurb: 'Patterns, structures, complexity' },
  { slug: 'languages', label: 'Programming Languages', blurb: 'C, C++, Java, Python, OOP and design patterns' },
  { slug: 'engineering', label: 'Engineering Practice', blurb: 'Backend, tooling, workflow, competitive programming' },
  { slug: 'finance', label: 'Finance', blurb: 'Markets, taxation, personal finance engineering' },
] as const;

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
