# 49. Group Anagrams

## Description

Given an array of strings, group anagrams together.

**Example**:

```txt
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

**Note**:

* All inputs will be in lowercase.
* The order of your output does not matter.

## Solution

### Sorting

* Sort each string

Use tuple as key

* Time Complexity: $O(NK \log K)$ ($O(N)$ loop, $O(K \log K)$ sorting)
* Space Complexity: $O(NK)$

### Counter

Group of the text

* same length
* same components

Use tuple as key

* Time Complexity: $O(NK)$
* Space Complexity: $O(NK)$

## Others' Solution

### Unique Prime Multiplication

```py
class Solution(object):
    def anagrams(self, strs):
        primes = {'a': 2,
                  'b': 3,
                  'c': 5,
                  'd': 7,
                  'e': 11,
                  'f': 13,
                  'g': 17,
                  'h': 19,
                  'i': 23,
                  'j': 29,
                  'k': 31,
                  'l': 37,
                  'm': 41,
                  'n': 43,
                  'o': 47,
                  'p': 53,
                  'q': 59,
                  'r': 61,
                  's': 67,
                  't': 71,
                  'u': 73,
                  'v': 79,
                  'w': 83,
                  'x': 89,
                  'y': 97,
                  'z': 101
                 }


        subLists = {}

        for string in strs:
            product = 1

            for character in string:
                product = primes[character] * product

            if product in subLists.keys():
                listA = subLists[product]
                listA.append(string)
                subLists[product] = listA
            else:
                subLists[product] = [string]

        listToReturn = []

        for value in subLists.keys():
            listToReturn.append(subLists[value])

        return listToReturn
```

### 2-line Python solution

* [2-line Python solution, AC with 350ms (some useful Python tricks) - LeetCode Discuss](https://leetcode.com/problems/group-anagrams/discuss/19203/2-line-Python-solution-AC-with-350ms-%28some-useful-Python-tricks%29)

```py
class Solution(object):
    def anagrams(self, strs):
        count = collections.Counter([tuple(sorted(s)) for s in strs])
        return filter(lambda x: count[tuple(sorted(x))] > 1, strs)
```
