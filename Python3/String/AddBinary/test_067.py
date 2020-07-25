from Adder067 import Solution as Adder
from Iterative067 import Solution as Iterative

testcase = [
    ('11', '1', '100'),
    ('1010', '1011', '10101')
]


def test_adder():
    for a, b, ans in testcase:
        assert Adder().addBinary(a, b) == ans


def test_iterative():
    for a, b, ans in testcase:
        assert Iterative().addBinary(a, b) == ans
