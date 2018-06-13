from DP070 import Solution as DynamicProgramming
from Recursive070 import Solution as Recursive

testcase = [1, 2, 3, 4, 5, 6]
answer = [1, 2, 3, 5, 8, 13]

def test_DynamicProgramming():
    for i, test in enumerate(testcase):
        assert DynamicProgramming().climbStairs(test) == answer[i]

def test_Recursive():
    for i, test in enumerate(testcase):
        assert Recursive().climbStairs(test) == answer[i]
