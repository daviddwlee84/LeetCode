from Naive957 import Solution as naive
from LoopDetection957 import Solution as loopdetection

testcase = [
    ([0, 1, 0, 1, 1, 0, 0, 1], 0, [0, 1, 0, 1, 1, 0, 0, 1]),
    ([0, 1, 0, 1, 1, 0, 0, 1], 1, [0, 1, 1, 0, 0, 0, 0, 0]),
    ([0, 1, 0, 1, 1, 0, 0, 1], 2, [0, 0, 0, 0, 1, 1, 1, 0]),
    ([0, 1, 0, 1, 1, 0, 0, 1], 3, [0, 1, 1, 0, 0, 1, 0, 0]),
    ([0, 1, 0, 1, 1, 0, 0, 1], 4, [0, 0, 0, 0, 0, 1, 0, 0]),
    ([0, 1, 0, 1, 1, 0, 0, 1], 5, [0, 1, 1, 1, 0, 1, 0, 0]),
    ([0, 1, 0, 1, 1, 0, 0, 1], 6, [0, 0, 1, 0, 1, 1, 0, 0]),
    ([0, 1, 0, 1, 1, 0, 0, 1], 7, [0, 0, 1, 1, 0, 0, 0, 0]),
    # ([1, 0, 0, 1, 0, 0, 1, 0], 1000000000, [0, 0, 1, 1, 1, 1, 1, 0])
]


def test_naive():
    for cells, N, ans in testcase:
        assert naive().prisonAfterNDays(cells, N) == ans


def test_loopdetection():
    for cells, N, ans in testcase:
        assert loopdetection().prisonAfterNDays(cells, N) == ans
