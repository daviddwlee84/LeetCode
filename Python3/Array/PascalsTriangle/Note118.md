# 118. Pascal's Triangle

## Description

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

> In Pascal's triangle, each number is the sum of the two numbers directly above it.

**Example**:

```txt
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

## Solution

### Naive

* Calculate using math definition: for each row $m$ on position $n$, the value is $C^m_n = \frac{m!}{n!(m-n)!}$

### Improve (TODO)

* Add memory to the function of `C`

## Others' Solution

### Recursive

```py
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return [] # Base Case
        if numRows == 1: return [[1]] # Base Case
        row = []
        last = self.generate(numRows - 1) # Recursion
        for i in range(numRows):
            if i == 0 or i == numRows - 1: row.append(1)
            else: row.append(last[-1][i-1] + last[-1][i])
        last.append(row)
        return last
```

### Iterative

```py
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1], [1, 1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return pascal[:1]
        elif numRows == 2:
            return pascal
        else:
            for i in range(2, numRows):
                line = [1]
                for j in range(1, i):
                    line.append(pascal[i-1][j -1] + pascal[i-1][j])
                line.append(1)
                pascal.append(line)
        return pascal
```

### Pythonic

```py
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1: return []
        pt = [[1]]
        
        for i in range(1, numRows):
            a = pt[-1]
            pt.append([1] + list(map(sum, zip(a, a[1:]))) + [1])
        return pt
```
