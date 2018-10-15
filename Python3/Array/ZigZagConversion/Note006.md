# 6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

## Solution

### Naive

* Time Complexity: O(n)

* Calculate each pattern's length
* Use index in pattern to specify which row to put in
* Combine each row and output the answer

### Others

#### Use python's negative index of list

```python
class Solution:
    def convert(self, s, numRows):
        # exit early if we don't have enough rows to make pattern
        if numRows < 2:
            return s

        combo = [''] * numRows
        i = 0
        row = -1

        # we add characters to strings (each string is array)
        for char in s:
            combo[i] += char
            if i == 0 or i == numRows - 1:
                row = -row
            i += row
        return ''.join(combo)
```

```python
class Solution:
    def convert(self, s, numRows):
        # exit early if we don't have enough rows to make pattern
        if numRows == 1:
            return s

        combo = [''] * numRows
        i = 0

        # we add characters to strings (each string is array)
        for char in s:
            combo[i] += char
            if i == 0:
                direction = 1
            elif i == numRows - 1:
                direction = -1
            i += direcction
        return ''.join(combo)
```