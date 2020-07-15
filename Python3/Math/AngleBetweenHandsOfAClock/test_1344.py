from Naive1344 import Solution as naive

testcase = [
    (12, 30, 165),
    (3, 30, 75),
    (3, 15, 7.5),
    (4, 50, 155),
    (12, 0, 0)
]


def test_naive():
    for hour, minutes, angle in testcase:
        assert round(naive().angleClock(hour, minutes), 5) == round(angle, 5)
