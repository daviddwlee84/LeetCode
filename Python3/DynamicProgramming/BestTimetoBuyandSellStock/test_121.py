from DP121 import Solution as DynamicProgramming

testcase = []
testcase.append([7,1,5,3,6,4])
testcase.append([7,6,4,3,1])

answer = []
answer.append(5)
answer.append(0)

def test_DynamicProgramming():
    for i, test in enumerate(testcase):
        assert DynamicProgramming().maxProfit(test) == answer[i]