# Longest Substring Without Repeating Characters

## Description

Given a string, find the length of the longest substring without repeating characters.

**Example 1**:

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

**Example 2**:

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3**:

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Solution

[LeetCode Official Solution](https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/)

### Naive

> Check all the substring one by one to see if it has no dupicate character.

* Time Complexity: O(n³)

### Sliding Window

> To check if a character is already in the substring, we can scan the substring, which leads to an O(n²) algorithm. But we can do better.
>
> By using HashSet as a sliding window, checking if a character in the current can be done in O(1).
>
> A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i, j)[i,j) (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we slide [i, j)[i,j) to the right by 11 element, then it becomes [i+1, j+1)[i+1,j+1) (left-closed, right-open).

* Time Complexity: O(2n)

### Sliding Window Optimized

> The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.

* Time Complexity: O(n)

### Others Solutions

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        d = {} # keep a dict for occurance of chars, to detect if repeat occurrs. value would be the index of the latest occurance.
        begin = res = 0
        for i, ch in enumerate(s):
            if ch not in d or (ch in d and d[ch] < begin):
                # if this is a new char never appeared before, or if it appeared prior to the current beginning of string.
                curr = i - begin + 1
                res = curr if curr > res else res
            else:
                # if this char occured since the beginning of string, then the begin point should be moved to that char's previous occurance index + 1.
                begin = d[ch] + 1
            d[ch] = i # either situation the char's occurance index updates to the current index.
        return res
```