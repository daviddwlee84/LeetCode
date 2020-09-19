from DP121 import Solution as DynamicProgramming
from Naive121 import Solution as Naive
from DP2_121 import Solution as RealDP

testcase = []
testcase.append([7, 1, 5, 3, 6, 4])
testcase.append([7, 6, 4, 3, 1])

answer = []
answer.append(5)
answer.append(0)


def test_DynamicProgramming():
    for i, test in enumerate(testcase):
        assert DynamicProgramming().maxProfit(test) == answer[i]


def test_Naive():
    for i, test in enumerate(testcase):
        assert Naive().maxProfit(test) == answer[i]


def test_RealDP():
    for i, test in enumerate(testcase):
        assert RealDP().maxProfit(test) == answer[i]
