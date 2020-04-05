from Greedy122 import Solution as PeakValley
from Tricky122 import Solution as Tricky
from Max122 import Solution as Max

testcase = []
testcase.append([7, 1, 5, 3, 6, 4])
testcase.append([1, 2, 3, 4, 5])
testcase.append([7, 6, 4, 3, 1])
testcase.append([])

answer = []
answer.append(7)
answer.append(4)
answer.append(0)
answer.append(0)


def test_Greedy():
    for i, case in enumerate(testcase):
        assert PeakValley().maxProfit(case) == answer[i]


def test_Tricky():
    for i, case in enumerate(testcase):
        assert Tricky().maxProfit(case) == answer[i]


def test_Max():
    for i, case in enumerate(testcase):
        assert Max().maxProfit(case) == answer[i]
