from Naive006 import Solution as naive

def test_naive():
    assert naive().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert naive().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert naive().convert("", 1) == ""