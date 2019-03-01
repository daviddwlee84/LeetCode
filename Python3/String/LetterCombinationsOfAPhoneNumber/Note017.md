# Letter Combinations of a Phone Number

## Description

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![phone keyboard](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

**Example**:

```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

## Solution

### Backtracking

* Time complexity: O(n!) (LeetCode solution is O(3^N + 4^M))
* Space complexity: (same as time complexity due to recursive call)
