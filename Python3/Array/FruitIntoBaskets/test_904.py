from Naive904 import Solution as Naive
from Greedy904 import Solution as Greedy
from SlidingWindow904 import Solution as SlidingWindow

testcases = [
    ([1, 2, 1], 3),
    ([0, 1, 2, 2], 3),
    ([1, 2, 3, 2, 2], 4),
    ([1, 0, 1, 4, 1, 4, 1, 2, 3], 5)
]


def test_Naive():
    for fruits, ans in testcases:
        assert Naive().totalFruit(fruits) == ans


def test_Greedy():
    for fruits, ans in testcases:
        assert Greedy().totalFruit(fruits) == ans


def test_SlidingWindow():
    for fruits, ans in testcases:
        assert SlidingWindow().totalFruit(fruits) == ans
