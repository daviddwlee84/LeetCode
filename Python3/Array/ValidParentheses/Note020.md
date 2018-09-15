# 20. Valid Parentheses

## Description

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1**:

```
Input: "()"
Output: true
```

**Example 2**:

```
Input: "()[]{}"
Output: true
```

**Example 3**:

```
Input: "(]"
Output: false
```

**Example 4**:

```
Input: "([)]"
Output: false
```

**Example 5**:

```
Input: "{[]}"
Output: true
```

## Solution

### Naive

* Time Complexity: O(n)

* Push the encountered open bracket into stack.
* Pop the stack when encounter close bracket and see if it is the corresponding one.

### Hash Table

* Time Complexity: O(n)

* Improve the time of searching the corresponding bracket.