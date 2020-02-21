from Sorting056 import Solution as sorting

testcase = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]])
]


def test_sorting():
    for intervals, answer in testcase:
        assert sorting().merge(intervals.copy()) == answer
