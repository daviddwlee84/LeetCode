from AllElementsInTwoBinarySearchTrees_Naive import Solution as Naive
from AllElementsInTwoBinarySearchTrees_DCMem import Solution as DCMem
from AllElementsInTwoBinarySearchTrees_XOR import Solution as XOR

testcase = [
    ([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]], [2, 7, 14, 8]),
    ([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]], [8, 0, 4, 4])
]


def test_naive():
    for arr, queries, ans in testcase:
        assert Naive().xorQueries(arr, queries) == ans


def test_dcmem():
    for arr, queries, ans in testcase:
        assert DCMem().xorQueries(arr, queries) == ans

def test_xor():
    for arr, queries, ans in testcase:
        assert XOR().xorQueries(arr, queries) == ans
