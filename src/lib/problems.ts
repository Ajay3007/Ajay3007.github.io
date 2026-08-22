import { getCollection, type CollectionEntry } from 'astro:content';

export type Problem = CollectionEntry<'problems'>;
export type Editorial = CollectionEntry<'editorials'>;

/**
 * The DSA problem system.
 *
 * `_data/problems.yml` was the one genuinely data-driven part of the Jekyll
 * site, and its shape is preserved. What is replaced is the plumbing: 17 topic
 * pages each re-implemented the same ~89 lines of Liquid, and a normalised diff
 * between any two of them was six lines.
 */

/**
 * The topic pages Jekyll served, with the URLs they served at.
 *
 * Listed explicitly rather than derived from the topic list, because the URLs
 * are what must not move — `/learning/dsa/tree/tree-problems/` does not follow
 * from the topic slug `tree`, and three of them (`arrays`, `strings`,
 * `searching-sorting`) sit under folders that are capitalised on disk.
 */
export const TOPIC_PAGES = [
  { topic: 'arrays',             title: 'Arrays',              url: '/learning/dsa/arrays/arrays-problems/',                           parent: '/learning/dsa/arrays/' },
  { topic: 'backtracking',       title: 'Backtracking',        url: '/learning/dsa/backtracking/backtracking-problems/',               parent: '/learning/dsa/backtracking/' },
  { topic: 'binary-search',      title: 'Binary Search',       url: '/learning/dsa/binary-search/binary-search-problems/',             parent: '/learning/dsa/binary-search/' },
  { topic: 'bit-manipulation',   title: 'Bit Manipulation',    url: '/learning/dsa/bit-manipulation/bit-manipulation-problems/',       parent: '/learning/dsa/bit-manipulation/' },
  { topic: 'dynamic-programming',title: 'Dynamic Programming', url: '/learning/dsa/dynamic-programming/dynamic-programming-problems/', parent: '/learning/dsa/dynamic-programming/' },
  { topic: 'graphs',             title: 'Graphs',              url: '/learning/dsa/graphs/graphs-problems/',                           parent: '/learning/dsa/graphs/' },
  { topic: 'greedy',             title: 'Greedy',              url: '/learning/dsa/greedy/greedy-problems/',                           parent: '/learning/dsa/greedy/' },
  { topic: 'hashing',            title: 'Hashing',             url: '/learning/dsa/hashing/hashing-problems/',                         parent: '/learning/dsa/hashing/' },
  { topic: 'heaps',              title: 'Heaps',               url: '/learning/dsa/heaps/heaps-problems/',                             parent: '/learning/dsa/heaps/' },
  { topic: 'intervals',          title: 'Intervals',           url: '/learning/dsa/intervals/intervals-problems/',                     parent: '/learning/dsa/intervals/' },
  { topic: 'linked-list',        title: 'Linked List',         url: '/learning/dsa/linked-list/linked-list-problems/',                 parent: '/learning/dsa/linked-list/' },
  { topic: 'queues',             title: 'Queues',              url: '/learning/dsa/queues/queues-problems/',                           parent: '/learning/dsa/queues/' },
  { topic: 'recursion',          title: 'Recursion',           url: '/learning/dsa/recursion/recursion-problems/',                     parent: '/learning/dsa/recursion/' },
  { topic: 'searching-sorting',  title: 'Searching & Sorting', url: '/learning/dsa/searching-sorting/searching-sorting-problems/',     parent: '/learning/dsa/searching-sorting/' },
  { topic: 'stacks',             title: 'Stacks',              url: '/learning/dsa/stacks/stacks-problems/',                           parent: '/learning/dsa/stacks/' },
  { topic: 'strings',            title: 'Strings',             url: '/learning/dsa/strings/strings-problems/',                         parent: '/learning/dsa/strings/' },
  { topic: 'tree',               title: 'Trees',               url: '/learning/dsa/tree/tree-problems/',                               parent: '/learning/dsa/tree/' },
] as const;

const DIFFICULTY_ORDER = { easy: 0, medium: 1, hard: 2 } as const;

export async function getProblems(topic?: string): Promise<Problem[]> {
  const all = await getCollection('problems');
  return all
    .filter((p) => !topic || p.data.topics.includes(topic))
    .sort(
      (a, b) =>
        DIFFICULTY_ORDER[a.data.difficulty] - DIFFICULTY_ORDER[b.data.difficulty] ||
        Number(a.data.id) - Number(b.data.id),
    );
}

export interface Stats {
  total: number;
  solved: number;
  percent: number;
  easy: number;
  medium: number;
  hard: number;
}

export function statsFor(problems: Problem[]): Stats {
  const by = (d: string) => problems.filter((p) => p.data.difficulty === d).length;
  const solved = problems.filter((p) => p.data.solved).length;
  return {
    total: problems.length,
    solved,
    percent: problems.length ? Math.round((solved / problems.length) * 100) : 0,
    easy: by('easy'),
    medium: by('medium'),
    hard: by('hard'),
  };
}

/** Every topic that appears on a problem, with its count. */
export async function getTopics(): Promise<{ topic: string; count: number; page?: string }[]> {
  const all = await getCollection('problems');
  const counts = new Map<string, number>();
  for (const p of all) for (const t of p.data.topics) counts.set(t, (counts.get(t) ?? 0) + 1);
  return [...counts]
    .map(([topic, count]) => ({
      topic,
      count,
      page: TOPIC_PAGES.find((t) => t.topic === topic)?.url,
    }))
    .sort((a, b) => b.count - a.count);
}

/**
 * Editorials keyed by the problem they solve. The relationship is declared
 * once, on the editorial, and read from both sides — the Jekyll site stored it
 * in both directions by hand and had two that disagreed.
 */
export async function getEditorialsByProblem(): Promise<Map<string, Editorial>> {
  const editorials = await getCollection('editorials', (e) => !e.data.draft);
  return new Map(editorials.map((e) => [String(e.data.problem_id), e]));
}
