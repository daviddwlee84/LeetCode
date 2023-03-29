# 48. Rotate Image

## Description

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

**Note**:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

**Example 1**:

```txt
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

**Example 2**:

```txt
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

## Solution

### Common

> Image the matrix as a paper card

1. Transpose
2. Horizontal Flip

## Others' Solution

* [A common method to rotate the image - LeetCode Discuss](https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image)

```cpp
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
void rotate(vector<vector<int> > &matrix) {
    reverse(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}

/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
void anti_rotate(vector<vector<int> > &matrix) {
    for (auto vi : matrix) reverse(vi.begin(), vi.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}
```

* [1 line in Python - LeetCode Discuss](https://leetcode.com/problems/rotate-image/discuss/18888/1-line-in-Python)

```py
class Solution(object):
    def rotate(self, matrix):
        matrix[::] = zip(*matrix[::-1])
```

```py
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # flip horizontally
        for i in range(n):
            for j in range(n/2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1- j] = tmp
```

## Wrong Answer

```py
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        (0, 0) -> (0, 2) -> (2, 2) -> (2, 0)
        (0, 1) -> (2, 1) -> (1, 2) -> (1, 0)
        """
        n = len(matrix)
        mid = len(matrix) // 2 + 1
        for i in range(mid):
            for k in range(mid - 1):
                # print((k + i, k), (k + i, n - k - 1), (n - (k + i) - 1, n - k - 1), (n - (k + i) - 1, k))
                # matrix[k + i][k], matrix[k + i][n - k - 1], matrix[n - (k + i) - 1][n - k - 1], matrix[n - (k + i) - 1][k] = matrix[n - (k + i) - 1][k], matrix[k + i][k], matrix[k + i][n - k - 1], matrix[n - (k + i) - 1][n - k - 1]
                print((k, k + i), (k, n - (k + i) - 1), (n - k - 1, n - (k + i) - 1), (k, n - (k + i) - 1))
                matrix[k + i][k], matrix[k + i][n - k - 1], matrix[n - (k + i) - 1][n - k - 1], matrix[n - (k + i) - 1][k] = matrix[n - (k + i) - 1][k], matrix[k + i][k], matrix[k + i][n - k - 1], matrix[n - (k + i) - 1][n - k - 1]

                # matrix[k + i][k], matrix[]
                # matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][j] = matrix[n - j - 1][j],  matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][n - j - 1]
```
