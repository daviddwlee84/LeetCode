from Naive1029 import Solution as naive
from Diff1029 import Solution as diff
from Sorting1029 import Solution as sorting

testcase = [
    ([[10, 20], [30, 200], [400, 50], [30, 20]], 110),
    ([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]], 1859)
]


def test_naive():
    for costs, ans in testcase:
        assert naive().twoCitySchedCost(costs) == ans

def test_diff():
    for costs, ans in testcase:
        assert diff().twoCitySchedCost(costs) == ans

def test_sorting():
    for costs, ans in testcase:
        assert sorting().twoCitySchedCost(costs) == ans
