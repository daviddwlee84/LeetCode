from BFS279 import Solution as BFS

ns = []
ns.append(12)
ns.append(13)

answer = []
answer.append(3)
answer.append(2)

def test_BFS():
    for n, ans in zip(ns, answer):
        assert BFS().numSquares(n) == ans