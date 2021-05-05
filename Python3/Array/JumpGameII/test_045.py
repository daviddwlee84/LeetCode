from BFS045 import Solution as BFS
from Greedy045 import Solution as Greedy
from DP045 import Solution as DP
from Greedy2_045 import Solution as Greedy2
testcases = [
    ([2, 3, 1, 1, 4], 2),
    ([2, 3, 0, 1, 4], 2),
    ([1, 2], 1)
]


def test_BFS():
    for nums, jumps in testcases:
        assert BFS().jump(nums) == jumps


def test_Greedy():
    for nums, jumps in testcases:
        assert Greedy().jump(nums) == jumps


def test_DP():
    for nums, jumps in testcases:
        assert DP().jump(nums) == jumps


def test_Greedy2():
    for nums, jumps in testcases:
        assert Greedy2().jump(nums) == jumps
