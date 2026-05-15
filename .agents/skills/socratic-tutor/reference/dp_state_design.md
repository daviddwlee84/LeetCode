# DP state design checklist

When a learner proposes "this is DP", do not let them write code until they
can answer all four questions below. Refusing to move on is the whole point.

## The four questions

1. **State.** *What does `dp[i]` mean — in plain English, no code?*
   - Bad: "the answer at index i"
   - Good: "the length of the longest increasing subsequence **ending at**
     index i"

2. **Transition.** *How is `dp[i]` computed from earlier states?*
   - Force them to write the recurrence on paper / in a comment before
     coding it.
   - If the recurrence has more than 2-3 cases, the state is probably wrong.

3. **Base case(s).** *What's `dp[0]` (or `dp[base]`)? Why?*
   - Often the bug is here, not in the recurrence.

4. **Where does the final answer live?**
   - `dp[n-1]`? `max(dp)`? `sum(dp)`? Some external accumulator?

## Heuristics for picking the state

- **1D, "ending at i":** subsequence problems — LIS, max subarray (Kadane's
  variant), longest valid parentheses.
- **1D, "considering first i":** prefix problems — house robber, climbing
  stairs.
- **2D `dp[i][j]`:** two strings (edit distance, LCS), grid (unique paths,
  min path sum), interval (matrix chain, palindrome substring).
- **`dp[i][k]` where k ≤ small constant:** "at most k transactions",
  "at most k bins", knapsack-with-capacity.
- **Bitmask `dp[mask][i]`:** TSP-ish, "visit a subset", set cover with n ≤ 20.
- **Tree DP:** `dp[v]` = best answer for subtree rooted at v. Often two
  values: `(included, excluded)`.

## Top-down vs bottom-up

Push the learner toward whichever they're shakier on:
- If they always reach for memoization → make them write bottom-up.
- If they always reach for tabulation → make them write the recursion +
  `@cache` first to verify the recurrence.

For most interview DP problems both are fine. The repo has many examples of
each (see `Python3/Array/MaximumSubarray/DP053.py` for bottom-up, see any
`TopDownDP*.py` for memoized).

## Optimizing space (after correctness)

- Many 2D DPs only depend on the previous row → 1D + rolling.
- Many "ending at i" DPs only need O(1) extras (Kadane's).
- Push the learner to first **get the unoptimized version passing**, then
  optimize.

## Common bugs to ask about

- "Does your transition double-count anything?"
- "Are your indices 0-based or 1-based? Be consistent."
- "Did you handle the empty input?"
- "If `i < 0` in the recurrence, what's the convention?"
