from Naive020 import Solution as stack
from Dict020 import Solution as hashtable

strings = ["()", "()[]{}", "(]", "([)]", "{[]}"]
answers = [True, True, False, False, True]

def test_stack():
    for i, s in enumerate(strings):
        assert stack().isValid(s) == answers[i]

def test_hashtable():
    for i, s in enumerate(strings):
        assert hashtable().isValid(s) == answers[i]
