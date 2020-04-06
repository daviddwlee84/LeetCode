from typing import List
from Counter049 import Solution as counter
from Naive049 import Solution as naive
from Sorting049 import Solution as sorting

testcases = [
    (["eat", "tea", "tan", "ate", "nat", "bat"],
    [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ])
]

def _test_same(lst1: List[List[str]], lst2: List[List[str]]):
    lst2 = [sorted(item) for item in lst2]
    for item in lst1:
        if sorted(item) in lst2:
            lst2.remove(sorted(item))
        else:
            return False
    
    if len(lst2) == 0:
        return True
    else:
        return False


def test_counter():
    for case, answer in testcases:
        assert _test_same(counter().groupAnagrams(case.copy()), answer.copy())

def test_naive():
    for case, answer in testcases:
        assert _test_same(naive().groupAnagrams(case.copy()), answer.copy())

def test_sorting():
    for case, answer in testcases:
        assert _test_same(sorting().groupAnagrams(case.copy()), answer.copy())
