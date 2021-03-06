from Naive011 import Solution as BruteForce
from TwoPointer011 import Solution as TwoPointer
from Naive2_011 import Solution as BruteForce2
from TwoPointer2_011 import Solution as TwoPointer2

heights = []
heights.append([1, 8, 6, 2, 5, 4, 8, 3, 7])
heights.append([2, 3])

answer = []
answer.append(49)
answer.append(2)


def test_BruteForce():
    for i, height in enumerate(heights):
        assert BruteForce().maxArea(height) == answer[i]


def test_TwoPointer():
    for i, height in enumerate(heights):
        assert TwoPointer().maxArea(height) == answer[i]


def test_BruteForce2():
    for i, height in enumerate(heights):
        assert BruteForce2().maxArea(height) == answer[i]


def test_TwoPointer2():
    for i, height in enumerate(heights):
        assert TwoPointer2().maxArea(height) == answer[i]
