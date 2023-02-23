from Naive2099 import Solution as Naive

testcases = [
    ({'nums': [2, 1, 3, 3], 'k': 2}, [3, 3]),
    ({'nums': [-1, -2, 3, 4], 'k': 3}, [-1, 3, 4]),
    # TODO: able to test => Return "any" such subsequence as an integer array of length k.
    # ({'nums': [3, 4, 3, 3], 'k': 2}, [3, 4]),
    ({'nums': [3, 4, 3, 3], 'k': 2}, [4, 3]),
    ({'nums': [50, -75], 'k': 2}, [50, -75]),
]


def test_Naive():
    for testcase, ans in testcases:
        assert Naive().maxSubsequence(**testcase) == ans
