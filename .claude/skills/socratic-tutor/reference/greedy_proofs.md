# Greedy proof patterns

Use these as scaffolding when a learner has proposed a greedy solution but
hasn't proved it correct. Pick the template that fits the problem shape and
have *them* fill in the blanks — don't fill them yourself.

## Template 1 — Exchange argument (most common)

> Suppose there is an optimal solution OPT that, at step k, makes a different
> choice than our greedy G. Show that we can replace OPT's choice at step k
> with G's choice and obtain a solution OPT' that is **no worse** than OPT
> and matches G in steps 1..k. Repeat for k+1, k+2, …; we end up with
> something equal to G that is at least as good as OPT. Therefore G is
> optimal.

Questions to ask the learner:

- What is "step k" in this problem? (an element to pick, a job to schedule, etc.)
- What is the greedy choice at step k? (the smallest, the earliest deadline, …)
- If you swap OPT's step-k choice for greedy's, what could go wrong? Why doesn't it?
- What invariant survives the swap? (Total cost ≤, number of items ≥, etc.)

Classic problems where this works: **Activity selection (#435)**, **Jump
Game II (#45)**, **Minimum number of arrows (#452)**, **Assign cookies (#455)**.

## Template 2 — Stays-ahead

> At every step, greedy is at least as good as OPT in some monotone metric.
> Concretely: after picking the i-th element, greedy's running value is ≥ (or
> ≤) OPT's by some metric. Induct on i; conclude that the final greedy value
> is at least as good as OPT.

Questions to ask:

- What's the monotone metric here? (number of items so far, current sum, position reached.)
- After step i, what inequality holds between greedy and OPT?
- What's the inductive step?

Classic problems: **Jump Game (#55)** (greedy stays ahead in max-reachable
index), **Gas Station (#134)** (greedy stays ahead in fuel-deficit).

## Template 3 — Matroid / cut-property (rare in interviews, useful to recognize)

If the problem can be phrased as "pick a maximum-weight independent set",
greedy works iff the structure is a matroid. Most interview problems aren't
matroids — but **MST** is the canonical case.

For this repo, mention only when relevant; don't deep-dive unless the learner
brings it up.

## Counter-examples are gold

When a greedy *doesn't* work, finding the smallest counter-example is a
faster route to understanding than fighting the proof:

- **Coin change with denominations {1, 3, 4} for amount 6**: greedy gives
  `4 + 1 + 1 = 3 coins`, optimal is `3 + 3 = 2 coins`. So greedy fails →
  must use DP.
- **0/1 knapsack with greedy by value/weight ratio**: trivial 3-item
  counter-example. Hence DP.

Have the learner construct one of these by hand if they're proposing greedy
for a known DP problem.

## Red flags that greedy probably *won't* work

- Problem has "optimal subset" with a numeric capacity constraint (smells
  like knapsack → DP).
- The choice at step k depends on **future** information, not just local.
- Brute-force counter-example exists with n ≤ 5.
