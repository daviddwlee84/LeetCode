from NaiveInPlace189 import Solution as naiveInPlace
from UseArray189 import Solution as useArray
from Simplest189 import Solution as simplest


k = []
k.append(3)
k.append(2)
k.append(20)

answer = []
answer.append([5,6,7,1,2,3,4])
answer.append([3,99,-1,-100])
answer.append([2,3,4,5,6,7,1])

# It need to maintain different testcase list or the tests will influence each other since pytest test the function simultaneously
# I've tried to use list.copy(), but it doesn't work.

testcase1 = []
testcase1.append([1,2,3,4,5,6,7])
testcase1.append([-1,-100,3,99])
testcase1.append([1,2,3,4,5,6,7])

def test_naiveInPlace():
    for i, case in enumerate(testcase1):
        naiveInPlace().rotate(case, k[i])
        assert case == answer[i]

testcase2 = []
testcase2.append([1,2,3,4,5,6,7])
testcase2.append([-1,-100,3,99])
testcase2.append([1,2,3,4,5,6,7])

def test_useArray():
    for i, case in enumerate(testcase2):
        useArray().rotate(case, k[i])
        assert case == answer[i]

testcase3 = []
testcase3.append([1,2,3,4,5,6,7])
testcase3.append([-1,-100,3,99])
testcase3.append([1,2,3,4,5,6,7]) # LeetCode's testcasse don't include rotate k times which k > 2*length

def test_simplest():
    for i, case in enumerate(testcase3):
        simplest().rotate(case, k[i])
        assert case == answer[i]