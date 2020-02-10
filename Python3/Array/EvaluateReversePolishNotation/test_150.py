from Stack150 import Solution as stack

testcase = [
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)
]


def test_stack():
    for tokens, output in testcase:
        assert stack().evalRPN(tokens) == output
