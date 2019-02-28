# Longest Palindromic Substring

## Description

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

**Example 1**:

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

**Example 2**:

```
Input: "cbbd"
Output: "bb"
```

## Solution

### Brute Force

> Time Limit Exceeded

For each possible substring, check if it's palindrom, and keep the longest one.

* Time Complexity: O(n³)
* Space Complexity: O(1)

### Dynamic Programming

* Time Complexity: O(n²)
* Space Complexity: O(n²)

### Expand Around Center

* Time Complexity: O(n²)
* Space Complexity: O(1)

### Others

* [Youtube Chinese Explination](https://youtu.be/m2Mk9JN5T4A)
