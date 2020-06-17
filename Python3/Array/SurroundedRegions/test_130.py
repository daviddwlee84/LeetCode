from Naive130 import Solution as naive
from Boarders130 import Solution as boarders

testcase = [
    ([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
     [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]),
    ([], []),
    ([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
     [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]])
]


def test_naive():
    for board, ans in testcase:
        temp = board.copy()
        naive().solve(temp)
        assert temp == ans


def test_boarders():
    for board, ans in testcase:
        temp = board.copy()
        boarders().solve(temp)
        assert temp == ans
