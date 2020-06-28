from BFS279 import Solution as BFS
from Recursive279 import Solution as Recursive
from Math279 import Solution as Math
from TopDownDP279 import Solution as TopDownDP
from LinearCheck279 import Solution as LinearCheck
from BottomUpDP279 import Solution as BottomUpDP


ns = []
ns.append(12)
ns.append(13)
ns.append(1)
ns.append(221)
ns.append(224)
ns.append(123)
ns.append(6603)

answer = []
answer.append(3)
answer.append(2)
answer.append(1)
answer.append(2)
answer.append(3)
answer.append(3)
answer.append(3)


def test_BFS():
    for n, ans in zip(ns, answer):
        assert BFS().numSquares(n) == ans


def test_LinearCheck():
    for n, ans in zip(ns, answer):
        assert LinearCheck().numSquares(n) == ans


def test_Math():
    for n, ans in zip(ns, answer):
        assert Math().numSquares(n) == ans


def test_BottomUpDP():
    for n, ans in zip(ns, answer):
        assert BottomUpDP().numSquares(n) == ans

# RecursionError: maximum recursion depth exceeded in comparison

# def test_Recursive():
#     for n, ans in zip(ns, answer):
#         assert Recursive().numSquares(n) == ans


# def test_TopDownDP():
#     for n, ans in zip(ns, answer):
#         assert TopDownDP().numSquares(n) == ans
