# 36. Valid Sudoku

## Description

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

**Example 1**:

```
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
```

**Example 2**:

```
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Note**:

* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.
* The given board contain only digits 1-9 and the character `'.'`.
* The given board size is always 9x9.

## Solution

### Hash Table

* Time Complexity: O(n) - go through each grid

* Build Hashtables for the three conditions that need to keep without repetition
    * Grid (Sub-boxes)
        * (another approach to index in one dimension array: row//3 * 3 + col//3)
    * Vertical Line (Column)
    * Horizontal Line (Row)

#### Shorter version

```python
class Solution:
    def isValidSudoku(self, board):
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        areas = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele == '.':
                    continue
                area_id = i // 3 * 3 + j // 3
                if ele in rows[i] or ele in cols[j] or ele in areas[area_id]:
                    return False
                else:
                    rows[i].append(ele)
                    cols[j].append(ele)
                    areas[area_id].append(ele)
        return True
```