# 151. Reverse Words in a String

## Description

Given an input string, reverse the string word by word.

**Example 1:**

```txt
Input: "the sky is blue"
Output: "blue is sky the"
```

**Example 2**:

```txt
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

**Example 3**:

```txt
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

**Note**:

* A word is defined as a sequence of non-space characters.
* Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
* You need to reduce multiple spaces between two words to a single space in the reversed string.

**Follow up**:

For C programmers, try to solve it *in-place* in O(1) extra space.

## Solution

### Pythonic

1. split words
2. concatenate words in reverse order

### Trick 1

1. reverse the individual words
2. reverse the whole string

## Other Language

C

* [Reverse words in a given string - GeeksforGeeks](https://www.geeksforgeeks.org/reverse-words-in-a-given-string/)
