from Greedy2405 import Solution as Greedy

testcases = [
    ("abacaba", 4),
    ("ssssss", 6),
]


def test_Greedy():
    for s, ans in testcases:
        assert Greedy().partitionString(s) == ans
