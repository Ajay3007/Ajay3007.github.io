# Ajdevhub — Complete Architecture Modernization & Knowledge Platform Migration

You are working on my personal GitHub Pages repository:

**My repository:**
https://github.com/Ajay3007/Ajay3007.github.io

I also want you to study this repository as an architectural/reference example:

**Reference repository:**
https://github.com/aspiremis/aspiremis.github.io

The reference repository belongs to a friend. Do NOT copy its content, personal information, branding, or blindly reproduce its implementation. Study its architecture, organization, content-driven design, reusable components, learning-system patterns, automation, and UX ideas.

---

# 1. CONTEXT

My current GitHub Pages site has evolved organically over time.

It contains:

* Learning notes
* DSA content
* DSA problems
* Projects
* Editorials
* Blog/posts
* Roadmaps
* Resources
* Technical notes
* Various custom UI components
* Data-driven DSA functionality
* Other personal/professional content

The current repository works, but the architecture has become messy and difficult to maintain.

A lot of the UI, navigation, pages, and relationships between content are manually maintained.

I now want to transform this repository into a **long-term personal Engineering Knowledge Platform**.

This is NOT merely a portfolio website.

The long-term goal is:

> Build a structured, searchable, interconnected representation of everything I learn, build, and explore as a software engineer.

---

# 2. MY LONG-TERM KNOWLEDGE DOMAINS

The platform should eventually support domains such as:

* AI / ML
* Neural Networks
* Deep Learning
* Transformers
* LLMs
* Graph Compilers
* Compiler Fundamentals
* Computational Graphs
* IR / Intermediate Representations
* Graph Optimization
* Hardware Acceleration
* Networking
* Dataplane
* DPDK
* Distributed Systems
* System Design
* C / C++
* Java
* Python
* DSA
* Algorithms
* Projects
* Research / Papers
* Books
* Courses
* Tools
* Engineering Resources

The exact taxonomy should NOT be hardcoded prematurely.

Design the system so that I can add new domains later without changing the application architecture.

---

# 3. VERY IMPORTANT: FIRST AUDIT, DO NOT MODIFY

Before changing ANYTHING:

## Completely audit my existing repository.

Inspect:

* Entire directory structure
* Existing Jekyll configuration
* Collections
* `_data`
* `_includes`
* `_layouts`
* Markdown files
* HTML files
* JavaScript
* CSS
* Scripts
* Build/deployment configuration
* GitHub Actions
* Existing search functionality
* DSA system
* Problem database
* Roadmaps
* Projects
* Posts
* Editorials
* Existing navigation
* Existing URLs
* Existing reusable components
* Existing special-case logic
* Existing SEO metadata
* Existing assets
* Existing dependencies

Also inspect the git history sufficiently to understand important architectural decisions.

DO NOT delete or rewrite anything during this phase.

---

# 4. STUDY THE REFERENCE REPOSITORY

Analyze:

https://github.com/aspiremis/aspiremis.github.io

Study especially:

* Overall architecture
* Content organization
* Astro usage
* Content Collections
* Schema validation
* Markdown/MDX approach
* Reusable components
* Layout system
* Learning tracks
* Modules
* Lessons
* Progress system
* Search
* Mathematical rendering
* GitHub Actions
* TypeScript usage
* Content metadata
* Navigation generation
* Prerequisites
* Related content
* UX patterns
* Responsive design
* Maintainability

Create a comparison:

```text
My current architecture
        ↓
Reference architecture
        ↓
What is worth adopting
        ↓
What should NOT be copied
        ↓
Recommended Ajdevhub architecture
```

---

# 5. DO NOT BLINDLY MIGRATE TO ASTRO

Evaluate whether migrating from Jekyll to Astro is actually the best decision.

I suspect Astro + TypeScript + Content Collections is a strong fit, but I want you to verify this based on my current repository.

Compare at least:

### Option A

Improve existing Jekyll architecture.

### Option B

Migrate to Astro.

### Option C

Another suitable static-site architecture.

Evaluate:

* Maintainability
* Content scalability
* Type safety
* Developer experience
* Build performance
* Search
* Markdown/MDX
* Dynamic content generation
* Learning progress
* Content relationships
* Math/code rendering
* GitHub Pages compatibility
* Migration complexity
* Long-term extensibility

Then make a recommendation.

If Astro is the best choice, use Astro.

Do not migrate simply because the reference repository uses Astro.

---

# 6. CORE ARCHITECTURAL PRINCIPLE

The most important architectural principle should be:

> **CONTENT SHOULD DRIVE THE UI.**

I should NOT have to manually update:

* Navigation
* Cards
* Breadcrumbs
* Related topics
* Previous/next links
* Search index
* Roadmap pages
* Topic indexes
* Category pages
* Learning progress pages

when I add a new piece of content.

For example, if I create:

```text
src/content/learning/ai/transformers/attention.md
```

with appropriate metadata, the system should automatically understand:

* Title
* Domain
* Category
* Topic
* Difficulty
* Status
* Prerequisites
* Related topics
* Tags
* Ordering
* Learning path
* Search metadata

and automatically update the appropriate UI.

---

# 7. PROPOSE A CONTENT MODEL

Design a scalable content schema.

Potential content types include:

```text
Learning Concepts
Courses / Tracks
Modules
Lessons
Notes
Problems
Projects
Roadmaps
Resources
Papers
Books
Tools
Editorials
Posts
```

Do NOT blindly implement all of them if they are unnecessary.

Create schemas with validation.

For example:

```yaml
title:
description:
domain:
category:
tags:
status:
difficulty:
prerequisites:
related:
order:
date:
```

Use strongly typed schemas where appropriate.

---

# 8. LEARNING SYSTEM

The new site should support a structured learning system.

I want to be able to represent:

```text
Domain
  ↓
Track
  ↓
Module
  ↓
Concept
  ↓
Sub-concepts
```

Example:

```text
AI / ML
  ↓
Neural Networks
  ↓
Foundations
  ↓
Forward Pass
  ↓
Matrix Multiplication
  ↓
Tensor
```

Another example:

```text
Compilers
  ↓
Graph Compiler
  ↓
Graph Optimization
  ↓
Operator Fusion
```

The hierarchy must be data-driven.

---

# 9. LEARNING STATUS

Every learning concept should optionally support status such as:

```text
not-started
learning
understood
solid
```

Do not force every piece of content to have a status.

The UI should be able to display learning progress automatically.

For example:

```text
Transformers

Embedding              ✓ Solid
Attention              ◐ Learning
Multi-Head Attention   ○ Not Started
Transformer Block      ○ Not Started
```

The exact visual design is up to you.

---

# 10. MENTAL MODEL SYSTEM

This is one of the most important features.

My goal is to build mental models rather than simply collect notes.

Each technical concept should be able to contain sections such as:

```text
What is it?
Why does it exist?
Intuition
Mental Model
Mathematical View
Example
Computational Graph
Implementation
Compiler Perspective
Hardware Perspective
Common Confusions
Prerequisites
Related Concepts
My Understanding
```

Do NOT force all sections to exist on every page.

The content author should decide what is appropriate.

---

# 11. KNOWLEDGE GRAPH / RELATED CONCEPTS

The system should support relationships between concepts.

For example:

```text
Attention
 ├── Tensor
 ├── Matrix Multiplication
 ├── Softmax
 ├── QKV
 └── Transformer Block
```

And:

```text
Operator Fusion
 ├── Computational Graph
 ├── Graph Optimization
 ├── IR
 ├── Memory Optimization
 └── Hardware Execution
```

I want these relationships to become navigable.

If possible, create reusable components for:

* Prerequisites
* Related concepts
* See also
* Next concept
* Previous concept
* Dependency graph

Do not over-engineer this initially.

---

# 12. GRAPH-COMPILER LEARNING

A major new learning area for me is:

> AI / ML → Computational Graphs → Graph Compiler → Hardware

The website should support this progression.

I want to eventually document concepts such as:

```text
Tensor
Operator
Computational Graph
Graph IR
Intermediate Representation
Graph Optimization
Constant Folding
Dead Node Elimination
Operator Fusion
Layout Transformation
Shape Inference
Quantization
Memory Planning
Scheduling
Lowering
Code Generation
Hardware Mapping
```

These should NOT contain proprietary company information.

They should represent generic technical knowledge.

---

# 13. IMPORTANT CONFIDENTIALITY RULE

I am working on a real internal Graph Compiler project at my company.

Some of my private Claude conversations may contain internal company documentation.

The public GitHub repository MUST NOT contain:

* Company confidential information
* Proprietary architecture
* Internal component names
* Internal APIs
* Internal algorithms
* Internal implementation details
* Internal performance numbers
* Internal benchmarks
* Internal chip specifications
* Internal diagrams
* Internal code
* Internal terminology that could expose the implementation
* Any copied text from confidential documents

The GitHub documentation should contain only:

* Generic technical concepts
* Publicly known concepts
* My own generalized understanding
* Public references
* Non-confidential examples

When helping me document something related to my work, prefer:

```text
Generic concept
+
General compiler explanation
+
General hardware perspective
```

rather than:

```text
Our internal implementation does X.
```

If there is uncertainty about whether something is safe to publish, flag it instead of publishing it.

---

# 14. DSA SYSTEM

My current repository already has a relatively data-driven DSA problem system.

Preserve the useful design principles from it.

I want a single source of truth for problems.

The system should be able to automatically generate:

* Problem listing
* Topic listing
* Difficulty filters
* Status
* Problem cards
* Problem details
* Related concepts
* Solution/editorial links

Do not destroy existing DSA content.

Migrate it carefully.

---

# 15. ROADMAP SYSTEM

I already maintain learning roadmaps.

Roadmaps should become data-driven.

For example:

```text
Roadmap
  ↓
Stage
  ↓
Topic
  ↓
Concept
```

The roadmap should automatically link to actual learning content.

For example:

```text
AI / ML Roadmap

Stage 1
 ├── Linear Algebra ✓
 ├── Probability
 └── Tensors

Stage 2
 ├── Neural Networks
 ├── Backpropagation
 └── Optimization

Stage 3
 ├── Transformers
 ├── Attention
 └── LLMs
```

Avoid maintaining the same information in multiple places.

---

# 16. SEARCH

Implement a proper static search solution suitable for GitHub Pages.

Evaluate Pagefind or an equivalent solution.

Search should be able to find:

* Concepts
* Notes
* DSA problems
* Projects
* Resources
* Roadmaps

Search results should clearly show:

* Title
* Category
* Type
* Short description
* Relevant match

---

# 17. UI / UX

Redesign the UI after the architecture is stable.

Desired characteristics:

* Clean
* Modern
* Technical
* Minimal
* Fast
* Responsive
* Excellent typography
* Excellent code rendering
* Excellent mathematical rendering
* Dark/light mode
* Keyboard-friendly navigation
* Mobile-friendly
* Accessible

Avoid:

* Excessive animations
* Overly flashy portfolio effects
* Huge hero sections
* Unnecessary gradients
* UI that prioritizes appearance over information

This is primarily a knowledge platform.

---

# 18. HOMEPAGE

The homepage should communicate:

1. Who I am
2. What I work on
3. What I'm currently learning
4. My major technical domains
5. My projects
6. My roadmaps
7. My knowledge base

Potential high-level structure:

```text
Ajay Gupta

Software Engineer
Systems • Networking • Dataplane • AI • Compilers

Currently Learning
------------------
Transformers → Graph Compilers

Knowledge Domains
------------------
AI / ML
Systems
Networking
Compilers
DSA
Java
C/C++

Projects
--------
...

Roadmaps
--------
...

Recently Updated
----------------
...
```

Use your judgment to improve this.

---

# 19. AUTOMATED UI

I want to minimize manual UI maintenance.

Automatically generate wherever appropriate:

* Navigation
* Sidebar
* Breadcrumbs
* Cards
* Topic indexes
* Domain indexes
* Related content
* Prerequisites
* Previous/next
* Search
* Roadmap references
* Learning progress
* Tags
* RSS/feed if useful
* Sitemap
* SEO metadata

Adding content should generally require adding/updating content metadata rather than editing UI code.

---

# 20. DESIGN SYSTEM

Create reusable components.

Potential components:

```text
Card
Badge
Tag
Breadcrumb
Sidebar
Search
ProgressIndicator
LearningStatus
PrerequisiteList
RelatedConcepts
CodeBlock
MathBlock
Callout
Diagram
Timeline
Roadmap
ProjectCard
ProblemCard
ResourceCard
```

Avoid creating one-off components unless necessary.

---

# 21. URL COMPATIBILITY

This is extremely important.

Before migration, generate a map of:

```text
Current URL → New URL
```

Preserve existing URLs wherever practical.

For URLs that must change:

* Add redirects where GitHub Pages allows.
* Preserve important legacy routes.
* Avoid breaking existing indexed pages.

Do NOT casually rename everything.

---

# 22. SEO

Preserve/improve:

* Page titles
* Meta descriptions
* Canonical URLs
* Open Graph metadata
* Twitter/social metadata
* Sitemap
* robots.txt
* Semantic HTML
* Structured metadata where useful

---

# 23. PERFORMANCE

The site should remain a static-first site.

Prefer:

* Static generation
* Minimal JavaScript
* Optimized assets
* Code splitting where appropriate
* No unnecessary client-side frameworks

Do not introduce a backend unless there is a compelling reason.

---

# 24. GITHUB ACTIONS

Create a clean CI/CD pipeline.

It should:

```text
Push
 ↓
Install
 ↓
Validate content
 ↓
Type check
 ↓
Build
 ↓
Run tests/checks
 ↓
Deploy
```

If a content schema is invalid, the build should fail with a useful error.

---

# 25. MIGRATION STRATEGY

DO NOT perform a destructive migration.

Create a staged plan.

Recommended approach:

```text
Phase 0
Audit

Phase 1
Architecture design

Phase 2
Create new foundation

Phase 3
Create content schemas

Phase 4
Create reusable UI

Phase 5
Migrate DSA

Phase 6
Migrate Learning

Phase 7
Migrate Projects

Phase 8
Migrate Roadmaps

Phase 9
Migrate remaining content

Phase 10
Search + SEO + performance

Phase 11
Visual redesign

Phase 12
Final validation
```

At each phase:

* Preserve content
* Preserve metadata
* Preserve links
* Validate build
* Check visual output
* Check mobile layout

---

# 26. DO NOT DELETE OLD CONTENT

Before migration:

Create a migration inventory.

For every current content item record:

```text
Old path
Content type
Title
Destination
Status
New path
Migration notes
```

No content should disappear silently.

If something is obsolete, mark it for review instead of deleting it automatically.

---

# 27. GIT STRATEGY

Do not make one giant commit.

Use logical commits such as:

```text
chore: add new site foundation
feat: add content schemas
feat: add learning layouts
feat: migrate DSA content
feat: migrate learning content
feat: add search
feat: add roadmap system
feat: redesign homepage
chore: improve CI
```

This will make rollback much easier.

---

# 28. CLAUDE CODE WORKFLOW

Follow this workflow:

## STEP 1 — AUDIT

Do not modify files.

Produce:

```text
CURRENT_ARCHITECTURE.md
```

containing:

* Current architecture
* Major components
* Content types
* Problems
* Technical debt
* Existing automation
* Existing features
* URLs
* Dependencies
* Deployment
* Migration risks

---

## STEP 2 — REFERENCE ANALYSIS

Produce:

```text
REFERENCE_ARCHITECTURE.md
```

Explain what architectural patterns from the reference repository are useful for Ajdevhub.

---

## STEP 3 — PROPOSED ARCHITECTURE

Produce:

```text
PROPOSED_ARCHITECTURE.md
```

Include:

* Directory structure
* Content model
* Schemas
* Component architecture
* Routing
* Search
* Learning system
* Roadmap system
* DSA system
* Progress system
* Deployment
* Migration strategy

Do NOT modify the production site yet.

---

## STEP 4 — MIGRATION PLAN

Produce:

```text
MIGRATION_PLAN.md
```

with:

* Phases
* Risks
* Dependencies
* Content mapping
* URL mapping
* Rollback strategy

STOP after this stage and show me the architecture and migration plan.

I will review it before implementation.

---

# 29. AFTER I APPROVE

Once I explicitly approve the architecture:

Implement the migration incrementally.

Do not make assumptions about destructive changes.

Whenever you encounter ambiguity:

* Prefer preserving existing functionality.
* Prefer backward compatibility.
* Prefer reusable architecture.
* Prefer content-driven solutions.
* Avoid unnecessary complexity.

---

# 30. FINAL QUALITY BAR

The finished repository should feel like:

> **A personal engineering knowledge platform maintained by a software engineer, not a manually assembled GitHub Pages website.**

The key properties should be:

```text
Content-driven
        +
Type-safe
        +
Automated
        +
Searchable
        +
Interconnected
        +
Maintainable
        +
Fast
        +
Responsive
        +
Extensible
```

And most importantly:

> **I should be able to learn a new technical concept and add one well-structured content file, and the website should automatically integrate that concept into the appropriate navigation, search, relationships, roadmap, and learning views.**

---

# 31. IMPORTANT FINAL RULE

Do not optimize for the number of features.

Optimize for:

**Simplicity + maintainability + excellent information architecture.**

If a feature requires excessive manual maintenance, redesign the architecture.

If two pieces of information are duplicated, find a single source of truth.

If the UI needs to be manually updated whenever content changes, improve the content model.

If something can be derived automatically, derive it rather than storing it twice.

The end result should make it easy for me to continuously build this knowledge base for many years.

Start now with **STEP 1 — repository audit only**.

Do not modify the repository yet.
