# 128. Longest Consecutive Sequence

## Description

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

**Example**:

```txt
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

## Solution

### Brute-Force

1. Find all the sequence for each number

* Time Complexity: $O(n^3)$

### Naive

1. Add all the appeared input into a table and check if there is any number in front of it.
2. Get the number with maximum value in the table

* Time Complexity: $O(n^2)$

### Sotring

* Time Complexity: $O(n\log n)$

### HashSet and Intelligent Sequence Building

Doing the same thing like Brute-Force did but maintain a hashset.

* Time complexity: $O(n)$

> Although the time complexity appears to be quadratic due to the while loop nested within the for loop, closer inspection reveals it to be linear. Because the while loop is reached only when currentNum marks the beginning of a sequence (i.e. currentNum-1 is not present in nums), the while loop can only run for $n$ iterations throughout the entire runtime of the algorithm. This means that despite looking like $O(n \cdot n)$ complexity, the nested loops actually run in $O(n + n) = O(n)$ time. All other computations occur in constant time, so the overall runtime is linear.
