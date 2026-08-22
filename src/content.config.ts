import { defineCollection } from 'astro:content';
import { glob, file } from 'astro/loaders';
import { z } from 'zod';
import { DOMAINS, STATUSES } from './consts';

/**
 * Content model
 * -------------
 * Two shapes, split on one rule:
 *   • Anything with a body to read is markdown under src/content/<name>/.
 *   • Anything that is a pure record is one JSON list — appending an entry is
 *     an object, not a new file.
 *
 * Everything is validated at build time, so a typo fails the build instead of
 * silently rendering a broken page. The Jekyll site had no validation at all,
 * which is how three permalinks came to collide and silently drop pages.
 *
 * Checks that a schema cannot express — URL uniqueness, URL preservation
 * against the 407 live URLs, prerequisite resolution and cycles, editorial ↔
 * problem integrity — live in scripts/validate-content.mjs.
 */

const domainSlugs = DOMAINS.map((d) => d.slug) as [string, ...string[]];
const domain = z.enum(domainSlugs);

const statusSlugs = STATUSES.map((s) => s.slug) as [string, ...string[]];

/** Fields every published thing carries, whatever its shape. */
const publishable = {
  title: z.string().min(1),
  /** Required. 354 Jekyll pages shared one meta description; never again. */
  description: z.string().min(1),
  tags: z.array(z.string()).default([]),
  updated: z.coerce.date().optional(),
  draft: z.boolean().default(false),
  /**
   * Confidentiality gate. `review` builds locally but fails a production
   * build, so "I'll check whether this is safe to publish later" cannot ship
   * by accident. See the brief's confidentiality rule.
   */
  visibility: z.enum(['public', 'review']).default('public'),
};

/** URL carried as data, not derived from the file path. */
const addressable = {
  /**
   * The URL this page must serve at. Absent = derive from domain + slug.
   *
   * This is the key migration decision: 52 of the Jekyll permalinks diverge
   * from their file path, so deriving URLs from structure would break live
   * links. Carrying the URL explicitly makes the migration lossless, and the
   * uniqueness check makes the old silent-collision bug impossible.
   */
  url: z.string().startsWith('/').optional(),
  /** Old URLs that must keep resolving — emitted as redirect stubs. */
  redirectFrom: z.array(z.string().startsWith('/')).default([]),
};

/* ==========================================================================
   Learning: Domain → Track → Module → Concept
   --------------------------------------------------------------------------
   Modules group concepts for display and never appear in URLs, so a track can
   be resequenced without breaking a link. Ordering lives in `order`, never in
   a filename prefix — the Jekyll tree encoded it three incompatible ways
   (p4-m13-, module-b9-, m17-, ch5-) and moving a page meant changing its URL.
   ========================================================================== */

const concepts = defineCollection({
  loader: glob({ base: './src/content/concepts', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    ...publishable,
    ...addressable,

    domain,
    /** Must match a tracks entry id. Checked by validate-content.mjs. */
    track: z.string().optional(),
    /** Must match a modules.json slug within that track. */
    module: z.string().optional(),
    order: z.number().default(99),

    /** The author's own claim. Optional: absent means "no claim made". */
    status: z.enum(statusSlugs as [string, ...string[]]).optional(),
    difficulty: z.enum(['foundational', 'intermediate', 'advanced']).optional(),

    /** Concept ids. Unresolvable ids fail the build, cycles fail the build. */
    prerequisites: z.array(z.string()).default([]),
    related: z.array(z.string()).default([]),

    estimatedMinutes: z.number().int().positive().optional(),
  }),
});

const tracks = defineCollection({
  loader: glob({ base: './src/content/tracks', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    ...publishable,
    ...addressable,
    tagline: z.string(),
    domain,
    order: z.number(),
    status: z.enum(['active', 'planned', 'paused']),
  }),
});

const modules = defineCollection({
  loader: file('./src/content/modules.json'),
  schema: z.object({
    id: z.string(),
    track: z.string(),
    slug: z.string(),
    title: z.string(),
    description: z.string(),
    order: z.number(),
    /** Roadmap stage label, e.g. "Phase 2". Free text: timing is a fact. */
    stage: z.string().optional(),
  }),
});

/* ==========================================================================
   DSA — the one part of the Jekyll site that was already data-driven.
   The 9-field schema is preserved verbatim; `concepts` is the one addition.
   ========================================================================== */

const problems = defineCollection({
  loader: file('./src/content/problems.json'),
  schema: z.object({
    id: z.string(),
    title: z.string(),
    platform: z.enum(['leetcode', 'gfg']),
    difficulty: z.enum(['easy', 'medium', 'hard']),
    topics: z.array(z.string()).min(1),
    solved: z.boolean().default(false),
    problem_url: z.string(),
    approach_url: z.string().default(''),
    solution_url: z.string().default(''),
    /** Concept ids this problem exercises — renders on both sides. */
    concepts: z.array(z.string()).default([]),
  }),
});

const editorials = defineCollection({
  loader: glob({ base: './src/content/editorials', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    ...publishable,
    ...addressable,
    /** Must resolve to a problems.json id. The Jekyll site had 2 that didn't. */
    problem_id: z.string(),
    date: z.coerce.date(),
    difficulty: z.enum(['easy', 'medium', 'hard']).optional(),
  }),
});

/* ========================================================================== */

const posts = defineCollection({
  loader: glob({ base: './src/content/posts', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    ...publishable,
    ...addressable,
    date: z.coerce.date(),
    domain: domain.optional(),
    featured: z.boolean().default(false),
  }),
});

const projects = defineCollection({
  loader: glob({ base: './src/content/projects', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    ...publishable,
    ...addressable,
    year: z.number().int(),
    status: z.enum(['active', 'completed', 'archived']).default('completed'),
    tech: z.array(z.string()).default([]),
    github: z.url().optional(),
    demo: z.url().optional(),
    featured: z.boolean().default(false),
    order: z.number().default(99),
  }),
});

const resources = defineCollection({
  loader: file('./src/content/resources.json'),
  schema: z.object({
    id: z.string(),
    title: z.string(),
    kind: z.enum(['book', 'course', 'paper', 'tool', 'reference', 'video']),
    author: z.string().optional(),
    url: z.url().optional(),
    description: z.string(),
    domains: z.array(domain).default([]),
    recommended: z.boolean().default(false),
  }),
});

export const collections = {
  concepts,
  tracks,
  modules,
  problems,
  editorials,
  posts,
  projects,
  resources,
};
