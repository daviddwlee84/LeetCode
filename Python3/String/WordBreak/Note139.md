# 139. Word Break

## Description

Given a **non-empty** string s and a dictionary *wordDict* containing a list of **non-empty** words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

**Note**:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

**Example 1**:

```txt
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2**:

```txt
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

**Example 3**:

```txt
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

## Solution

### Recursive with Memory

1. Split string into small parts
2. If a parts is in wordDict then search the rest part

### (bottom-up) Dynamic Programming

> bottom-up mean calculate from `dp[0]` to `dp[n]` (=> calculate `dp[0]` first ---> `dp[n]`)

* Define: `dp[i]` is true if the *word break* of substring 0 to i is true.

## Others' Solution

* [Word Break Problem | Dynamic Programming | GeeksforGeeks - YouTube](https://www.youtube.com/watch?v=hLQYQ4zj0qg)

```py
class Solution:

    def wordBreak(self, s, di):
        l = len(s)
        cache = [False] * l
        di = sorted(di, key = len)
        def _wordBreak(start):
            if cache[start]:
                return False

            for w in di:
                newstart = start + len(w)
                if newstart > l:
                    break
                if s.startswith(w, start):
                    if newstart == l or _wordBreak(newstart):
                        return True
            cache[start] = True
            return False

        return _wordBreak(0)
```

* [Naive DFS with Memorize in Python - LeetCode Discuss](https://leetcode.com/problems/word-break/discuss/466036/Naive-DFS-with-Memorize-in-Python)

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        flag = [0 for i in range(n+1)]
        def helper(start):
            if flag[start]:
                return flag[start]==1
            if start==n:
                return True
            for word in wordDict:
                if s[start:start+len(word)]==word:
                    if helper(start+len(word)):
                        flag[start+len(word)] = 1
                        return True
                    else:
                        flag[start+len(word)] = -1
            return False
        return helper(0)
```

* [Simple Python recursion solution. Faster than 99.60% - LeetCode Discuss](https://leetcode.com/problems/word-break/discuss/463642/Simple-Python-recursion-solution.-Faster-than-99.60)

```py
def wordBreak(self, s: str, wordDict: List[str], res=False) -> bool:
    wordDict.sort(key=len, reverse=True)
    if s.isdigit() or res == True:  return True
    for word in wordDict:
        if word in s:  res = self.wordBreak(s.replace(word, '1'), wordDict, res)
    return res
```

* [Clean Python DP with explanation - LeetCode Discuss](https://leetcode.com/problems/word-break/discuss/461731/Clean-Python-DP-with-explanation)

```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        if not wordDict:
            return False

        length_set = set()
        word_set = set(wordDict)
        for w in word_set:
            length_set.add(len(w))

        # Init Boundary condition
        f = [False] * (len(s)+1)
        f[0] = True

        for i in range(1, len(s)+1):
            for l in length_set:
                if i >= l and f[i-l] and s[i-l:i] in word_set:
                    f[i] = True
                    break
        return f[-1]
```
