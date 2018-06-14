from DP198 import Solution as DynamicProgramming

testcase = []
testcase.append([1,2,3,1])
testcase.append([2,7,9,3,1])
testcase.append([2,1,1,2])

answer = []
answer.append(4)
answer.append(12)
answer.append(4)

def test_DP():
    for i, test in enumerate(testcase):
        assert DynamicProgramming().rob(test) == answer[i]
