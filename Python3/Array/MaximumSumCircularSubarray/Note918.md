# 918. Maximum Sum Circular Subarray

## Description

Given a **circular array C** of integers represented by `A`, find the maximum possible sum of a non-empty subarray of **C**.

Here, a *circular array* means the end of the array connects to the beginning of the array.  (Formally, `C[i] = A[i]` when `0 <= i < A.length`, and `C[i+A.length] = C[i]` when `i >= 0`.)

Also, a subarray may only include each element of the fixed buffer `A` at most once.  (Formally, for a subarray `C[i], C[i+1], ..., C[j]`, there does not exist `i <= k1, k2 <= j` with `k1 % A.length = k2 % A.length`.)

**Example 1**:

```txt
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
```

**Example 2**:

```txt
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
```

**Example 3**:

```txt
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
```

**Example 4**:

```txt
Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
```

**Example 5**:

```txt
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
```

**Note**:

* `-30000 <= A[i] <= 30000`
* `1 <= A.length <= 30000`

> Hint:
>
> 1. For those of you who are familiar with the Kadane's algorithm, think in terms of that. For the newbies, Kadane's algorithm is used to finding the maximum sum subarray from a given array. This problem is a twist on that idea and it is advisable to read up on that algorithm first before starting this problem. Unless you already have a great algorithm brewing up in your mind in which case, go right ahead!
>
> 2. What is an alternate way of representing a circular array so that it appears to be a straight array? Essentially, there are two cases of this problem that we need to take care of. Let's look at the figure below to understand those two cases:
>
>     ![hint](https://assets.leetcode.com/uploads/2019/10/20/circular_subarray_hint_1.png)
> 
> 3. The first case can be handled by the good old Kadane's algorithm. However, is there a smarter way of going about handling the second case as well?

## Note

* [Official Solution](https://leetcode.com/problems/maximum-sum-circular-subarray/solution/)
* [Maximum subarray problem - Kadane's algorithm - Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm)

About the Approaches

In both Approach 1 and Approach 2, "grindy" solutions are presented that require less insight, but may be more intuitive to those with a solid grasp of the techniques in those approaches. Without prior experience, these approaches would be very challenging to emulate.

Approaches 3 and 4 are much easier to implement, but require some insight.

### Explanation of Kadane's Algorithm

To understand the solutions in this article, we need some familiarity with Kadane's algorithm. In this section, we will explain the core idea behind it.

For a given array `A`, Kadane's algorithm can be used to find the maximum sum of the subarrays of `A`. Here, we only consider non-empty subarrays.

Kadane's algorithm is based on dynamic programming. Let `dp[j]` be the maximum sum of a subarray that ends in `A[j]`. That is,

$$
\text{dp}[j] = \max\limits_i (A[i] + A[i+1] + \cdots + A[j])
$$

Then, a subarray ending in `j+1` (such as `A[i], A[i+1] + ... + A[j+1]`) maximizes the `A[i] + ... + A[j]` part of the sum by being equal to `dp[j]` if it is non-empty, and 0 if it is. Thus, we have the recurrence:

$$
\text{dp}[j+1] = A[j+1] + \max(\text{dp}[j], 0)
$$

Since a subarray must end somewhere, $\max\limits_j dp[j]$ must be the desired answer.

To compute dp efficiently, Kadane's algorithm is usually written in the form that reduces space complexity. We maintain two variables: `ans` as $\max\limits_j dp[j]$], and `cur` as $dp[j]$; and update them as $j$ iterates from $0$ to $A\text{.length} - 1$.

Then, Kadane's algorithm is given by the following psuedocode:

```py
# Kadane's algorithm
ans = cur = None
for x in A:
    cur = x + max(cur, 0)
    ans = max(ans, cur)
return ans
```

### Approach 1: Next Array

```py
class Solution(object):
    def maxSubarraySumCircular(self, A):
        N = len(A)

        ans = cur = None
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)

        # ans is the answer for 1-interval subarrays.
        # Now, let's consider all 2-interval subarrays.
        # For each i, we want to know
        # the maximum of sum(A[j:]) with j >= i+2

        # rightsums[i] = sum(A[i:])
        rightsums = [None] * N
        rightsums[-1] = A[-1]
        for i in xrange(N-2, -1, -1):
            rightsums[i] = rightsums[i+1] + A[i]

        # maxright[i] = max_{j >= i} rightsums[j]
        maxright = [None] * N
        maxright[-1] = rightsums[-1]
        for i in xrange(N-2, -1, -1):
            maxright[i] = max(maxright[i+1], rightsums[i])

        leftsum = 0
        for i in xrange(N-2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i+2])
        return ans
```

### Approach 2: Prefix Sums + Monoqueue

### Approach 3: Kadane's (Sign Variant)

### Approach 4: Kadane's (Min Variant)

## Solution

## Others' Solution

---

## Fail

```py
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """ we only care about continuous positive value,
        naive way to check circularly is copy the array twice
        """
        data = [(val, i) for i, val in enumerate(A)] * 2
        num_used = set()
        global_max = 0
        temp_max = 0
        for value, idx in data:
            if idx not in num_used:
                if temp_max + value > 0:
                    temp_max += value
                    num_used.add(idx)
                else:
                    temp_max = 0
                    num_used = set()

                global_max = max(temp_max, global_max)

        return global_max
```

## Resources

### Tutorial

* [Maximum Sum Circular Subarray | LeetCode 918 | C++, Java, Python | May LeetCoding Day 15 | Kadane - YouTube](https://www.youtube.com/watch?v=os4B7MlHAbs)
