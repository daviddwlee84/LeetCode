from TwoPointer167 import Solution as twoPointer

numbers = []
numbers.append([2, 7, 11, 15])

targets = []
targets.append(9)

answer = []
answer.append([1, 2])

def test_twoPointer():
    for nums, target, ans in zip(numbers, targets, answer):
        assert twoPointer().twoSum(nums, target) == ans
