from Naive020 import Solution as stack

strings = ["()", "()[]{}", "(]", "([)]", "{[]}"]
answers = [True, True, False, False, True]

def test_stack():
    for i, s in enumerate(strings):
        assert stack().isValid(s) == answers[i]
