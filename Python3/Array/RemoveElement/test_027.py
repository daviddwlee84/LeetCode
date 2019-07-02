from Naive027 import Solution as naive
from Naive2027 import Solution as naive2

testcase = []
testcase.append([3,2,2,3])
testcase.append([0,1,2,2,3,0,4,2])
vals = []
vals.append(3)
vals.append(2)

returnLen = []
returnLen.append(2)
returnLen.append(5)
newArray = []
newArray.append([2,2])
newArray.append([0,1,3,0,4])

def test_naive():
    for i, (case, val) in enumerate(zip(testcase, vals)):
        array = case.copy()
        length = naive().removeElement(array, val)
        assert length == returnLen[i]
        assert sorted(array[:length]) == sorted(newArray[i])

def test_naive2():
    for i, (case, val) in enumerate(zip(testcase, vals)):
        array = case.copy()
        length = naive2().removeElement(array, val)
        assert length == returnLen[i]
        assert sorted(array[:length]) == sorted(newArray[i])
