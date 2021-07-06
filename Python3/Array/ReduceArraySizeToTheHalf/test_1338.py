from Naive1338 import Solution as naive


testcases = [
    ([3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2),
    ([7, 7, 7, 7, 7, 7], 1),
    ([1, 9], 1),
    ([1000, 1000, 3, 7], 1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
]


def test_naive():
    for arr, ans in testcases:
        assert naive().minSetSize(arr) == ans
