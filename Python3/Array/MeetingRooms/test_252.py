from interval import listToInterval
from Sorting252 import Solution as sorting

testcase = [
    (listToInterval([[0, 30], [5, 10], [15, 20]]), False),
    (listToInterval([[0, 5], [5, 10], [15, 20]]), True),
]


def test_sorting():
    for intervals, ans in testcase:
        assert sorting().canAttendMeetings(intervals) == ans
