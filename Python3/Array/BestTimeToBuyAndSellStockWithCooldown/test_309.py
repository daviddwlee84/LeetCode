from StateMachine309 import Solution as state_machine
from DP309 import Solution as DP
from StateMachine_DP309 import Solution as StateMachine_DP


testcase = [
    ([1, 2, 3, 0, 2], 3),
    ([1], 0),
]


def test_state_machine():
    for prices, ans in testcase:
        assert state_machine().maxProfit(prices) == ans


def test_DP():
    for prices, ans in testcase:
        assert DP().maxProfit(prices) == ans


def test_StateMachine_DP():
    for prices, ans in testcase:
        assert StateMachine_DP().maxProfit(prices) == ans
