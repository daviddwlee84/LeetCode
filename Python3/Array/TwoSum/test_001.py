from Naive001 import Solution as naive

def test_naive():
    assert naive().twoSum((2, 7, 11, 15), 9) == [0, 1]
    assert naive().twoSum((-3, 4, 3, 90), 0) == [0, 2]
