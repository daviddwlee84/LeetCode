from Greedy881 import Solution as Greedy

testcases = [
    ([1, 2], 3, 1),
    ([3, 2, 2, 1], 3, 3),
    ([3, 5, 3, 4], 5, 4),
]


def test_Greedy():
    for people, limit, ans in testcases:
        assert Greedy().numRescueBoats(people, limit) == ans
