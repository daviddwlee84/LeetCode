from Iterative704 import Solution as Iterative
from Recursive704 import Solution as Recursive
from Bisect704 import Solution as Bisect


testcases = [
    ({'nums': [-1, 0, 3, 5, 9, 12], 'target': 9}, 4),
    ({'nums': [-1, 0, 3, 5, 9, 12], 'target': 2}, -1),
    ({'nums': [-1, 0, 3, 5, 9, 12], 'target': 13}, -1),
]


def test_Iterative():
    for testcase, ans in testcases:
        assert Iterative().search(**testcase) == ans


def test_Recursive():
    for testcase, ans in testcases:
        assert Recursive().search(**testcase) == ans


def test_Bisect():
    for testcase, ans in testcases:
        assert Bisect().search(**testcase) == ans
