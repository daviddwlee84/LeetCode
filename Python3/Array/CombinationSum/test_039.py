from Backtracking039 import Solution as Backtracking
from Naive039 import Solution as naive

candidates_target = [
    ([2, 3, 6, 7], 7),
    ([2, 3, 5], 8),
    ([8, 7, 4, 3], 11)
]

answer = []
answer.append([
    [7],
    [2, 2, 3],

])
answer.append([
    [2, 2, 2, 2],
    [2, 3, 3],
    [3, 5]
])
answer.append([
    [3, 4, 4],
    [3, 8],
    [4, 7]
])


def test_backtracking():
    for i, (candidates, target) in enumerate(candidates_target):
        assert sorted(Backtracking().combinationSum(
            candidates, target)) == sorted(answer[i])


def test_naive():
    for i, (candidates, target) in enumerate(candidates_target):
        assert sorted((sorted(ans) for ans in naive().combinationSum(
            candidates, target))) == sorted(answer[i])
