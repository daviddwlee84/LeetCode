from Naive007 import Solution as naive

def test_naive():
    assert naive().reverse(123) == 321
    assert naive().reverse(-123) == -321
    assert naive().reverse(120) == 21
    assert naive().reverse(2**32-1) == 0