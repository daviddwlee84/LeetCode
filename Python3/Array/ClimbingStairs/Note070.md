# 70. Climbing Stairs

## Description

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Note**: Given n will be a positive integer.

**Example 1**:

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2**:

```
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Hint

To reach nth step, what could have been your previous steps? (Think about the step sizes)

## Solution

### Dynamic Programming

* Time Complexity: O(n)

1. method to first stair = 1
2. method to second stair = 2
3. method to n stair = method to n-2 stair (Climb another two step) + method to n-1 stair (Climb another one step)

* Classic Fibonacci Series: f(n) = f(n-1) + f(n-2)

### Recursive

(LeetCode: Time Limit Exceeded)

Same train of thought as dynamic programming

* Time Complexity without memorization: O(1.6180ⁿ) ([ex1](https://www.geeksforgeeks.org/time-complexity-recursive-fibonacci-program/), [ex2](https://stackoverflow.com/questions/360748/computational-complexity-of-fibonacci-sequence))
* Space Complexity without memorization: O(n) - Due to call stack


* Time Complexity with memorization: O(n)