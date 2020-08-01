from StateMachine309 import Solution as state_machine
from DP309 import Solution as DP


testcase = [
    ([1, 2, 3, 0, 2], 3)
]


def test_state_machine():
    for prices, ans in testcase:
        assert state_machine().maxProfit(prices) == ans


def test_DP():
    for prices, ans in testcase:
        assert DP().maxProfit(prices) == ans
