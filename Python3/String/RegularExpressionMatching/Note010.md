# Regular Expression Matching

## Description

Given an input string (`s`) and a pattern (`p`), implement regular expression matching with support for `'.'` and `'*'`.
```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```

The matching should cover the **entire** input string (not partial).

**Note**:

* s could be empty and contains only lowercase letters a-z.
* p could be empty and contains only lowercase letters a-z, and characters like . or *.

**Example 1**:
```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2**:
```
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

**Example 3**:
```
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

**Example 4**:
```
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
```

**Example 5**:
```
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```

## Solution

[LeetCode Official Solution](https://leetcode.com/problems/regular-expression-matching/solution/)

### Divide and Conquer

The solution without `*`

```python
def match(text, pattern):
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])
```

* If there's a star
    * we may ignore this part of the pattern, or delete a matching character in the text
* If we have a match on the remaining strings after any of these operations, then the initial inputs matched

### Dynamic Programming

**Intuition**

As the problem has an optimal substructure, it is natural to cache intermediate results. We ask the question `dp(i, j)`: does `text[i:]` and `pattern[j:]` match? We can describe our answer in terms of answers to questions involving smaller strings.

**Algorithm**

We proceed with the same recursion as in Divide and Conquer, except because calls will only ever be made to `match(text[i:], pattern[j:])`, we use `dp(i, j)` to handle those calls instead, saving us expensive string-building operations and allowing us to cache the intermediate results.

#### Top-down approach

#### Bottom-up approach

### Others

```python
class Solution:
    def isMatch(self, s, p):
        return self.helper(s, 0, p, 0, {})

    def helper(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i,j)]
        if len(p) == j: return len(s) == i
        if len(s) == i:
            if (len(p)-j) %2 == 1: return False
            index = j + 1
            while index < len(p) :
                if p[index] != '*':
                    return False
                index += 2
            return True
        if len(p) - j > 1 and p[j + 1] == '*' :
            if self.is_char_matched(s[i], p[j]):
                matched = self.helper(s, i+1, p, j, memo) or self.helper(s, i , p , j + 2, memo)
            else:
                matched = self.helper(s, i, p, j + 2, memo)
        else:
            matched = self.is_char_matched(s[i], p[j]) and self.helper(s, i + 1, p, j + 1, memo)
        memo[(i,j)] = matched
        return matched

    def is_char_matched(self, s, p):
        return s == p or p == "."
```

```python
class Solution:
    def isMatch(self, s, p):
        p = p[::-1]
        s = s[::-1]
        m, n = len(s), len(p)
        dp = [[False for j in range(n+1)] for i in range(m+1)]
        dp[-1][-1] = True
        j = 0
        while j < n:
            if p[j] == '*':
                dp[-1][j+1] = dp[-1][j-1]
                for i in range(m):
                    if dp[i][j-1]:
                        dp[i][j+1] = True
                    elif dp[i-1][j+1]:
                        dp[i][j+1] = (s[i] == p[j+1]) or (p[j+1]=='.')
                j += 1
            else:
                for i in range(m):
                    if p[j] == s[i] or p[j] == '.':
                        dp[i][j] = dp[i-1][j-1]
            j += 1
        return dp[m-1][n-1]
```