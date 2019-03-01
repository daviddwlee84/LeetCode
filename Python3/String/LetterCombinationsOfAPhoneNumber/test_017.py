from Backtracking017 import Solution as Backtracking

numbers = []
numbers.append("23")
numbers.append("")

answer = []
answer.append(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
answer.append([])


def test_backtracking():
    for i, nums in enumerate(numbers):
        assert Backtracking().letterCombinations(nums) == answer[i]
