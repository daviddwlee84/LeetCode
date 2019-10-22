from Naive069 import Solution as Naive

testcase = [
    (4, 2),
    (8, 2),
    (0, 0),
    (1, 1),
    (2, 1)
]

def test_naive():
    for x, ans in testcase:
        assert Naive().mySqrt(x) == ans
