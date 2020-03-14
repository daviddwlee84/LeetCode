from interval import listToInterval
from Sorting253 import Solution as sorting

testcase = [
    (listToInterval([[0, 30], [5, 10], [15, 20]]), 2),
    (listToInterval([[7, 10], [2, 4]]), 1),
]


def test_sorting():
    for intervals, ans in testcase:
        assert sorting().minMeetingRooms(intervals) == ans
