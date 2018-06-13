from Naive053 import Solution as BruteForce
from DP053 import Solution as DynamicProgramming
from DC053 import Solution as DivideAndConquer

testcase = []
testcase.append([-2,1,-3,4,-1,2,1,-5,4])
testcase.append([-1, 2])
testcase.append([-1])
testcase.append([1, 2])

answer = []
answer.append(6)
answer.append(2)
answer.append(-1)
answer.append(3)

# LeetCode: Time Limit Exceeded
def test_BruteFore():
    for i, test in enumerate(testcase):
        assert BruteForce().maxSubArray(test) == answer[i]

def test_DynamicProgramming():
    for i, test in enumerate(testcase):
        assert DynamicProgramming().maxSubArray(test) == answer[i]
    

def test_DivideAndConquer():
    for i, test in enumerate(testcase):
        assert DivideAndConquer().maxSubArray(test) == answer[i]