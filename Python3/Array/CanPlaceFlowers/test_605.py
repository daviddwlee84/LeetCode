from Naive605 import Solution as Naive

testcases = [
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False),
    ([1, 0, 0, 0, 0, 1], 2, False),
    ([1, 0, 0, 0, 0, 0, 1], 2, True),
    ([1, 0, 0, 0, 1, 0, 0], 2, True),
    ([0, 0, 0, 0, 0, 1, 0, 0], 0, True),
]


def test_Naive():
    for flowerbed, n, ans in testcases:
        assert Naive().canPlaceFlowers(flowerbed, n) == ans
