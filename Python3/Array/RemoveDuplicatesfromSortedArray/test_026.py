from Naive026 import Solution as naive
from Better026 import Solution as better

testcase = []
testcase.append([1,1,2])
testcase.append([0,0,1,1,1,2,2,3,3,4])

returnLen = []
returnLen.append(2)
returnLen.append(5)

newArray = []
newArray.append([1,2])
newArray.append([0,1,2,3,4])

def test_naive():
    for i, case in enumerate(testcase):
        rtn = naive().removeDuplicates(case)
        assert rtn == returnLen[i]
        assert case == newArray[i]

def test_better():
    for i, case in enumerate(testcase):
        rtn = better().removeDuplicates(case)
        assert rtn == returnLen[i]
        assert case == newArray[i]