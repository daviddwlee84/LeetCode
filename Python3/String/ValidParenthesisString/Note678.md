# 678. Valid Parenthesis String

## Description

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5. An empty string is also valid.

**Example 1**:

```txt
Input: "()"
Output: True
```

**Example 2**:

```txt
Input: "(*)"
Output: True
```

**Example 3**:

```txt
Input: "(*))"
Output: True
```

**Note**:

1. The string size will be in the range [1, 100].

## Solution

### Brute Force

* For each asterisk ('*') try both possibilities

* Time Complexity: O(N * 3^N)
  * 3^N Strings
  * Check of validity is O(N)

### Dynamic Programming

### Greedy

## Others' Solution

* [Official](https://leetcode.com/problems/valid-parenthesis-string/solution/)

Greedy

```py
class Solution(object):
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0
```
