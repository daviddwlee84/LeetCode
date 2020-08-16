# Dynamic Programming

## Beforehand

### What can DP do

* apply DP to **optimization problems**

### Optimal Substructure

> optimal solutions to a problem incorporate optimal solutions to related subproblems, which we may solve independently

### Subproblem Graphs

## How to find DP solution

### Tips of finding DP solution

It's hard to figure out DP solution at the first glance.

1. Find recursive solution first
    * Base Case
    * Recursive Case
2. Use recursive solution to derive DP formula
    * Recursive relationship - relationship between status i and any other previous status
3. Transform to DP form
    * Use a table/array/... to store the status (dp[i] for the ith status)
    * Base Case => Initialize dp[]
    * Recursive Case => Calculate dp[i]
4. Optimize space complexity
    * Consider what information dp[i] is depending on.
    * Only keep the necessary information and get rid of other sub-result

### Steps for developing a DP algorithm (Introduction to Algorithm)

1. Characterize the structure of an optimal solution
2. Recursively define the value of an optimal solution
3. Compute the value of an optimal solution, typically in a bottom-up fashion
4. Construct an optimal soluiton from computed information

> * Step 1~3: form the basis of a DP solution to a problem
> * If we need only the value of an optimal solution, and not the solution itself, then we can omit Step 4.
> * When we do perform step 4, we sometimes maintain additional information during Step 3 so that we can easily construct and optimal solution

## Resources

* [Dynamic Programming – From Novice to Advanced](https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/)
* [DP IS EASY! 5 Steps to Think Through DP Questions. - LeetCode Discuss](https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.)
* [What does a state represent in terms of Dynamic Programming? - Quora](https://www.quora.com/What-does-a-state-represent-in-terms-of-Dynamic-Programming)
* [**How to solve DP - String? Template and 4 Steps to be followed. - LeetCode Discuss**](https://leetcode.com/discuss/general-discussion/651719/how-to-solve-dp-string-template-and-4-steps-to-be-followed)

### Tutorial

* [Dynamic Programming lecture #1 - Fibonacci, iteration vs recursion - YouTube](https://www.youtube.com/watch?v=YBSt1jYwVfU)
* [Dynamic Programming lecture #2 - Coin change, double counting - YouTube](https://www.youtube.com/watch?v=1mtvm2ubHCY)
* [Dynamic Programming lecture #3 - Line of wines - YouTube](https://www.youtube.com/watch?v=pwpOC1dph6U)

### Book

Introduction to Algorithm

* Ch15 Dynamic Programming
  * Ch15.1 Rod cutting
    * optimal substructure
    * subproblem graph
  * Ch15.2 Matrix-chain Multiplication
  * Ch15.3 Elements of Dynamic Programming
    * Optimal substructure
    * Overlapping subproblems
    * Reconstructing an optimal soluiton
    * Memoization
  * Ch15.4 Longest Common Subsequence - [note 1143](../../Python3/String/LongestCommonSubsequence/Note1143.md)
