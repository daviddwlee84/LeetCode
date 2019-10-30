# 72. Edit Distance

## Description

Given two words *word1* and *word2*, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

**Example 1**:

```txt
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

**Example 2**:

```txt
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Study

Summary

> determine the DP table row by row

* If the character is different: take the minimum of three (left, top-left, top) plus one
* If the character is the same: just take the diagonal (top-left)
* The last number (the (m, n) number of DP table) is the answer

## Solution

### Recursive

* Time Complexity: $O(m^n)$
* Space Complexity: $O(m^n)$

### Dynamic Programming

* Time Complexity: $O(m \times n)$
* Space Complexity: $O(m \times n)$ (can be optimize to $O(n)$)

1. Use a table to store the optimal result
   1. Table size with (m+1)x(n+1)
   2. Initial the first column and first row of table to be 0 to length
2. Compare character by character => to see when the new char come, what operation can we apply to make two words be the same
   * use the conclusion of the rules

## Others' Solution

* [C++ O(n)-space DP - LeetCode Discuss](https://leetcode.com/problems/edit-distance/discuss/25846/C%2B%2B-O%28n%29-space-DP) - optimize the space complexity
* [Python solutions and intuition - LeetCode Discuss](https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition) - from recursive to caching to dynamic programming

## Resources

* [Minimum Edit Distance Dynamic Programming - YouTube](https://www.youtube.com/watch?v=We3YDTzNXEk) - good whiteboard explaination
  * edit
  * delete
  * add
* [MIT Edit Distance - YouTube](https://youtu.be/ocZMDMZwhCY?t=1457)
* [Edit Distance Between 2 Strings - The Levenshtein Distance ("Edit Distance" on LeetCode) - YouTube](https://www.youtube.com/watch?v=MiqoA-yF-0M)
* [Minimum Edit Distance - Explained ! - Stanford University - YouTube](https://www.youtube.com/watch?v=Xxx0b7djCrs)
