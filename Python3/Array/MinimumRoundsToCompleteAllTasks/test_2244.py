from Greedy2244 import Solution as Greedy
from Greedy2_2244 import Solution as Greedy2

testcases = [
    ([2, 2, 3, 3, 2, 4, 4, 4, 4, 4], 4),
    ([2, 3, 3], -1),
    ([5, 5, 5, 5], 2),
    ([66, 66, 63, 61, 63, 63, 64, 66, 66, 65, 66, 65, 61, 67, 68, 66, 62, 67, 61, 64, 66, 60, 69, 66, 65, 68,
     63, 60, 67, 62, 68, 60, 66, 64, 60, 60, 60, 62, 66, 64, 63, 65, 60, 69, 63, 68, 68, 69, 68, 61], 20),
]


def test_Greedy():
    for tasks, ans in testcases:
        assert Greedy().minimumRounds(tasks) == ans

def test_Greedy2():
    for tasks, ans in testcases:
        assert Greedy2().minimumRounds(tasks) == ans
