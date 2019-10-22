from Adder067 import Solution as Adder

testcase = [
    ('11', '1', '100'),
    ('1010', '1011', '10101')
]

def test_adder():
    for a, b, ans in testcase:
        assert Adder().addBinary(a, b) == ans