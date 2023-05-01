from Naive1491 import Solution as Naive

testcases = [
    ([4000, 3000, 1000, 2000], 2500.0),
    ([1000, 2000, 3000], 2000.0),
]

# Answers within 10-5 of the actual answer will be accepted.


def test_Naive():
    for salary, ans in testcases:
        assert Naive().average(salary) == ans
