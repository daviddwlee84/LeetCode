from Naive1249 import Solution as Naive
from Naive2_1249 import Solution as Naive2
testcase = [
    ("lee(t(c)o)de)", {"lee(t(c)o)de", "lee(t(c)ode)", "lee(t(co)de)"}),
    ("a)b(c)d", {"ab(c)d"}),
    ("))((", {""}),
    ("(a(b(c)d)", {"a(b(c)d)", "(a(bc)d)", "(ab(c)d)"}),
]


def test_naive():
    for s, answers in testcase:
        assert Naive().minRemoveToMakeValid(s) in answers


def test_naive2():
    for s, answers in testcase:
        assert Naive2().minRemoveToMakeValid(s) in answers
