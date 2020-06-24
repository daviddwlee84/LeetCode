from DP174 import Solution as dp

testcase = [
    ([[-2, -3, 3],
      [-5, -10, 1],
      [10, 30, -5]], 7),
    ([[0]], 1),
    ([[-10]], 11),
    ([[10]], 1),
    ([[0, 5],
      [-2, -3]], 1)
]


def test_dp():
    for dungeon, ans in testcase:
        assert dp().calculateMinimumHP(dungeon) == ans
