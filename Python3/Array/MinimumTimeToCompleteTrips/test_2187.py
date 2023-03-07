from BinarySearch2187 import Solution as BinarySearch

testcases = [
    ([1, 2, 3], 5, 3),
    ([2], 1, 2),
]


def test_BinarySearch():
    for time, totalTrips, ans in testcases:
        assert BinarySearch().minimumTime(time, totalTrips) == ans
