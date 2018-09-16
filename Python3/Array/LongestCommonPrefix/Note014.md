# 14. Longest Common Prefix

## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1**:

```
Input: ["flower","flow","flight"]
Output: "fl"
```

**Example 2**:

```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Note**:

All given inputs are in lowercase letters `a-z`.

## Solution

### Naive

* Time Complexity: O(n * length) = O(S) (total characters in all strings)

* Find the shortest string length to build a loop.
* Compare each character one by one, if all same append in the prefix or end the program.

### Others

[Official Solution](https://leetcode.com/problems/longest-common-prefix/solution/)

```python
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        strs = sorted(strs, key=lambda s: len(s))

        i = len(strs[0])
        while i > 0:
            if all(x.startswith(strs[0][:i]) for x in strs):
                return strs[0][:i]
            else:
                i-= 1
        return ''
```

```python
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Use any of strings as reference, choose the first one for convenience
        if len(strs) == 0:
            return ""

        referenceString = strs[0]
        common = ""

        for i in range(len(referenceString)):
            char = referenceString[i]
            for ele in strs:
                if i < len(ele):
                    if ele[i] != char:
                        return common
                else:
                    return common
            common += char
        return common
```