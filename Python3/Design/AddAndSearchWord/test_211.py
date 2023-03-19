from Naive211 import WordDictionary as naive
from RegEx211 import WordDictionary as regex
from Tire211 import WordDictionary as tire
from Tire2_211 import WordDictionary as tire2

testcase = [
    (["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
     [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
     [None, None, None, None, False, True, True, True]),
    (["WordDictionary", "addWord", "addWord", "addWord", "addWord", "search", "search", "addWord", "search", "search", "search", "search", "search", "search"],
     [[], ["at"], ["and"], ["an"], ["add"], ["a"], [".at"], ["bat"],
         [".at"], ["an."], ["a.d."], ["b."], ["a.d"], ["."]],
     [None, None, None, None, None, False, False, None, True, True, False, False, True, False]),
]


def class_test(totest):

    obj = None
    for ops, vals, anss in testcase:
        for op, val, ans in zip(ops, vals, anss):
            if op == "WordDictionary":
                obj = totest()
            elif op == "addWord":
                assert obj.addWord(val[0]) == ans
            elif op == "search":
                assert obj.search(val[0]) == ans
            else:
                assert False


def test_naive():
    class_test(naive)


def test_regex():
    class_test(regex)


def test_tire():
    class_test(tire)


def test_tire2():
    class_test(tire2)
