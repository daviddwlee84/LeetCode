from Greedy857 import Solution as greedy
from GreedyPQ857 import Solution as greedyPQ

testcase = [
    ({
        'quality': [10, 20, 5],
        'wage': [70, 50, 30],
        'K': 2,
    }, 105.00000),
    ({
        'quality': [3, 1, 10, 10, 1],
        'wage': [4, 8, 2, 2, 7],
        'K': 3,
    }, 30.66667),
]


def test_greedy():
    for case, ans in testcase:
        round(greedy().mincostToHireWorkers(**case), 5) == ans


def test_greedyPQ():
    for case, ans in testcase:
        round(greedyPQ().mincostToHireWorkers(**case), 5) == ans
