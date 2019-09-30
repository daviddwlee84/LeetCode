from Naive038 import Solution as Naive

answer = [
    "1",
    "11",
    "21",
    "1211",
    "111221",
    "312211"
]


def test_naive():
    for i, ans in enumerate(answer):
        assert Naive().countAndSay(i+1) == ans
