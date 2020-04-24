from Backtracking055 import Solution as backtracking
from DPTopDown055 import Solution as DPtopdown
from DPBottomUp055 import Solution as DPbottomup
from Greedy055 import Solution as greedy

testcase = [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([0], True),
    ([2, 0], True),
    ([1, 2, 0, 1], True)
]


def test_backtracking():
    for nums, ans in testcase:
        assert backtracking().canJump(nums) == ans


def test_DPtopdown():
    for nums, ans in testcase:
        assert DPtopdown().canJump(nums) == ans


def test_DPbottomup():
    for nums, ans in testcase:
        assert DPbottomup().canJump(nums) == ans


def test_greedy():
    for nums, ans in testcase:
        assert greedy().canJump(nums) == ans
