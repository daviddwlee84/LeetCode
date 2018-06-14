from Naive001 import Solution as naive
from HashTable001 import Solution as hashTable
from SortedHashTable001 import Solution as sortedHashTable

testnums = []
testtargets = []
answer = []

testnums.append([2, 7, 11, 15])
testtargets.append(9)
answer.append([0,1])

testnums.append([-3, 4, 3, 90])
testtargets.append(0)
answer.append([0,2])

testnums.append([3,2,4])
testtargets.append(6)
answer.append([1,2])


def test_naive():
    for i in range(len(testnums)):
        assert naive().twoSum(testnums[i], testtargets[i]) == answer[i]

def test_hashTable():
    for i in range(len(testnums)):
        assert hashTable().twoSum(testnums[i], testtargets[i]) == answer[i]

def test_sortedHashTable():
    for i in range(len(testnums)):
        assert sortedHashTable().twoSum(testnums[i], testtargets[i]) == answer[i]