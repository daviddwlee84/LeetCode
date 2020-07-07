from Naive079 import Solution as naive
from DFS079 import Solution as DFS
from DFS2_079 import Solution as DFS2

testcase = [
    ([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], "ABCCED", True),
    ([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], "SEE", True),
    ([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], "ABCB", False),
    ([
        ['a']
    ], "a", True),
    ([
        ['a', 'a']
    ], "aaa", False)
]


def test_naive():
    for board, word, ans in testcase:
        assert naive().exist(board, word) == ans


def test_DFS():
    for board, word, ans in testcase:
        assert DFS().exist(board, word) == ans


def test_DFS2():
    for board, word, ans in testcase:
        assert DFS2().exist(board, word) == ans
