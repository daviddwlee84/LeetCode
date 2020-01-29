from BFS200 import Solution as BFS
from DFS200 import Solution as DFS

testcase = []
testcase.append(
"""
11110
11010
11000
00000
"""
)
testcase.append(
"""
11000
11000
00100
00011
"""
)
testcase.append(
""
)
testcase.append(
"""
111
010
111
"""
)

answer = []
answer.append(1)
answer.append(3)
answer.append(0)
answer.append(1)


def _str_to_list(strings: str):
    return [list(row) for row in strings.split()]


def test_BFS():
    for test, num in zip(testcase, answer):
        grid = _str_to_list(test)
        assert BFS().numIslands(grid) == num


def test_DFS():
    for test, num in zip(testcase, answer):
        grid = _str_to_list(test)
        assert DFS().numIslands(grid) == num
