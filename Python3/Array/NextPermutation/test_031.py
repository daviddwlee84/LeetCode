from SinglePass031 import Solution as SinglePass

inputs = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 1, 5],
    [1],
    [1, 3, 2]
]

answer = [
    [1, 3, 2],
    [1, 2, 3],
    [1, 5, 1],
    [1],
    [2, 1, 3]
]

def test_singlepass():
    for i, nums in enumerate(inputs):
        SinglePass().nextPermutation(nums)
        assert nums == answer[i]
