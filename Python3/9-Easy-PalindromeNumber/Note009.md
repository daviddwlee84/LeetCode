# 9. Palindrome Number (回文數字)

## Description

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

**Example 1:**

```
Input: 121
Output: true
```

**Example 2:**

```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Follow up:**

Coud you solve it without converting the integer to a string?


## Solution

### Naive

* Time Complexity: O(n/2)

Convert to a string and compare each index from beggining and end.

### Without Converting to a String

* Time Complexity: O(n)
* Key: Compare original number with reverse one

1. Negative number isn't palindrome number
2. 0 is palindrome number
3. Reverse entire number (as A)
    1. Initialize A with 0; B with input value
    2. Update A with A*10 + B%10 (Extract each numbers with %10)
    3. Update B with B/10
    4. Do until B equal 0
4. Compare the A with input value