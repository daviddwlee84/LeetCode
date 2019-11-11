# 300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

```txt
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Note**:

* There may be more than one LIS combination, it is only necessary for you to return the length.
* Your algorithm should run in $O(n^2)$ complexity.

**Follow up**: Could you improve it to $O(n \log n)$ time complexity?

## Solution

### Brute Force

* Find all increasing subsequence and then returning the maximum length of LIS.

**Cases**:

1. Current num > previous num
   1. include the current element in LIS
2. Current num < previous num
   1. skip current num

Return the max length of either taken current num or skip current num

**Complexity**:

* Time complexity: $O(2^n)$ - size of recursion tree
* Space complexity: $O(n^2)$

### Recursion with Memoization

* Time complexity: $O(n^2)$ - size of recursion tree
* Space complexity: $O(n^2)$

### Dynamic Programming

if we know the length of the LIS upto $i^{th}$ index, we can figure out the length of the LIS possible by including the $(i+1)^{th}$ element based on the elements with indices $j$ such that $0 \leq j \leq (i + 1)$

$$
dp[i]=\max(dp[j])+1, \forall 0 \leq j<i
$$
$$
LIS_{length} = \max(dp[i]), \forall 0 \leq i<n
$$

* Time complexity: $O(n^2)$
* Space complexity: $O(n)$

### Binary Search Trick

* Made a Binary Search function that
  * when found the number, return the index itself
  * if not found then return `-(insertion point) - 1`
* Maintain an array that try too keep each number as small as possible

```txt
This method is NOT based on binary search in DP
swipe through the array, maintain a subsequence array s of INCREASING numbers for each new element x
if x larger than s[s.size()-1], append x to s
else find an element that's just larger than x (whose previous is smaller than x) replace that element with x (above can be done with binary search)

Why is this correct? s is NOT the increasing subsequence we're looking for
However, the length of s is the correct answer
when we replace s[i] with x
we don't change the length of answer, but we changed the potential best candidate
the idea is to try to make each position's number as small as possible
the actual sequence only changes when we append a number, otherwise it's just a
"virtual change", meaning we don't change the current sequence, but we try to
make each number small so we'll have a larger chance to append more numbers
```

* Time complexity: $O(n\log n)$ - Binary Search
* Space complexity: $O(n)$ - the array

## Resources

* [Longest Increasing Subsequence - LeetCode Articles](https://leetcode.com/articles/longest-increasing-subsequence/)
