# 91. Decode Ways

## Description

A message containing letters from `A-Z` is being encoded to numbers using the following mapping:

```txt
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given a **non-empty** string containing only digits, determine the total number of ways to decode it.

**Example 1**:

```txt
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2**:

```txt
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

## Solution

### Backtracking (Brute Force)

### Dynamic Programming

---

Wrong Answer

```py
class Solution:

    def numDecodings(self, s: str) -> int:
        def helper(s: str):
            if len(s) > 0 and s[0] == '0':
                return 0, False
            if len(s) == 0:
                return 0, True
            elif len(s) == 1:
                return 1, True
            elif len(s) == 2:
                if s == '10':
                    return 1, True
                elif 26 >= int(s) >= 11:
                    return 2, True

            drop1, valid1 = helper(s[1:])
            if int(s[:2]) <= 26:
                drop2, valid2 = helper(s[2:])
            else:
                drop2, valid2 = 0, False

            return drop1 + drop2, valid1 or valid2

        ans, valid = helper(s)
        if not valid:
            return 0
        return ans
```