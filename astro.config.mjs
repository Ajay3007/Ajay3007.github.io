// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';

/**
 * ajdevhub — Astro build.
 *
 * This coexists with the Jekyll site during the migration: Jekyll builds from
 * `_layouts/`, `_learning/`, `_posts/` …; Astro builds from `src/` into `dist/`.
 * Neither reads the other's files, and `_config.yml` excludes everything here,
 * so production stays on Jekyll until the Phase 11 cutover.
 *
 * A GitHub *user* site lives at the domain root, so there is no `base` to set —
 * which avoids the whole class of broken-asset bugs that project pages cause.
 */
export default defineConfig({
  site: 'https://ajay3007.github.io',

  // The Jekyll site serves every page as a directory URL (`/learning/dsa/`),
  // and 401 of the 407 live URLs depend on that shape being preserved.
  trailingSlash: 'always',
  build: { format: 'directory' },

  /**
   * Emitted as static redirect pages, since GitHub Pages has no server-side
   * redirects. Used only where a page genuinely moves — everything else keeps
   * its URL via the `url` field on the content entry.
   */
  redirects: {
    // The hand-maintained master list is superseded by the generated hub.
    '/learning/dsa/master-problem-list/': '/problems/',
    // about.md had no permalink, so Jekyll served it as a file.
    '/about.html': '/about/',
    // This one permalink omitted its trailing slash, so Jekyll wrote a file
    // where every sibling is a directory.
    '/learning/programming-language/cpp/lambda-functions.html':
      '/learning/programming-language/cpp/lambda-functions/',
    // An empty category page in Jekyll; no post carries the tag.
    '/blogs/competitive-programming/': '/blogs/',
  },

  integrations: [
    mdx(),
    sitemap({
      filter: (page) => !page.includes('/404'),
    }),
  ],

  markdown: {
    // Astro 7 deprecates markdown.remarkPlugins / rehypePlugins in favour of
    // passing a unified processor directly.
    processor: unified({
      remarkPlugins: [
        // The AI/ML and graph-compiler tracks are unwritable without math:
        // softmax, attention, shape inference. Rendered at build time, so no
        // math library ships to the browser.
        remarkMath,
      ],
      rehypePlugins: [
        rehypeKatex,
        rehypeSlug,
        [
          // Anchor links on headings — a 1,400-line module page needs its
          // sections to be directly linkable.
          rehypeAutolinkHeadings,
          {
            behavior: 'append',
            properties: { className: ['heading-anchor'], ariaHidden: 'true', tabIndex: -1 },
            content: { type: 'text', value: '#' },
          },
        ],
      ],
    }),
    shikiConfig: {
      // One render serves both themes — no client-side highlighting.
      themes: { light: 'github-light', dark: 'github-dark-dimmed' },
      wrap: true,
    },
  },

  vite: {
    plugins: [tailwindcss()],
  },
});
