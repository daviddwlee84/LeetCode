# Complexity analysis quick reference

Use to corroborate the learner's analysis in Phase 6 — but ask them to derive
it first, then check against this.

## Common shapes

| Pattern                                  | Time           | Space (extra) |
|------------------------------------------|----------------|---------------|
| Single pass over array                   | O(n)           | O(1)          |
| Nested loop over same array              | O(n²)          | O(1)          |
| Sort + scan                              | O(n log n)     | O(1) or O(n)  |
| Hash table lookup                        | O(n) avg       | O(n)          |
| Binary search on sorted                  | O(log n)       | O(1)          |
| Recursion: T(n) = 2 T(n/2) + O(n)        | O(n log n)     | O(log n) stack |
| Recursion: T(n) = 2 T(n-1) + O(1)        | O(2ⁿ)          | O(n) stack    |
| DP `dp[i]` 1D                            | O(n)           | O(n) → O(1) rolling |
| DP `dp[i][j]` 2D                         | O(n·m)         | O(n·m) → O(min(n,m)) rolling |
| Bitmask DP over subsets of {0..n-1}      | O(2ⁿ · n)      | O(2ⁿ)         |
| BFS / DFS on graph                       | O(V + E)       | O(V)          |
| Dijkstra (binary heap)                   | O((V+E) log V) | O(V)          |
| Topological sort (Kahn's)                | O(V + E)       | O(V)          |
| Union-Find with path compression + rank  | O(α(n)) per op | O(n)          |

## Recursion depth → space

Always count stack frames as space. A "linear time DFS on a tree" is
**O(n) time, O(h) space** where h is the height (n in the worst case).

## "Best you can do" sanity checks

- Read the input → at least O(n).
- Output a permutation → at least O(n!) or you missed something.
- Comparison-based sorting → at least O(n log n).
- Find the median of an unsorted array → expected O(n) (Quickselect), worst
  O(n²); deterministic O(n) exists but rarely asked.

## Amortized vs worst case

Be precise. Common gotchas:

- Dynamic-array `append` is **O(1) amortized**, not worst-case.
- `dict[k] = v` is **O(1) amortized expected**, worst-case O(n) on
  adversarial keys.
- Quicksort is **O(n log n) expected**, **O(n²) worst**.
- Path-compressed Union-Find is **O(α(n)) amortized per op**.

If the interviewer asks "is this O(1)", the right answer is often "amortized
O(1), worst-case O(n)".

## When the user reports a complexity

Make them justify it by counting:

- "How many times does the outermost loop run?"
- "For each of those, how much work does the body do?"
- "Multiply."

If they wave their hands, ask for a small concrete n (n=4, n=8) and have
them count operations. The pattern usually pops out.
