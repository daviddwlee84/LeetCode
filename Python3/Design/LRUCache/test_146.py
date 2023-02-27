from Naive146 import LRUCache as Naive
from OrderedDict146 import LRUCache as OrderedDict
from Queue146 import LRUCache as Queue
from DoubleLinkedList146 import LRUCache as DoubleLinkedList
from typing import List


testcase = [
    (["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
     [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
     [None, None, None, 1, None, -1, None, -1, 3, 4]),
    (["LRUCache", "put", "put", "get", "put", "put", "get"],
     [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]],
     [None, None, None, 2, None, None, -1])
]


def helper(instructions: List[str], values: List[int], answer: List[int], cacheClass):
    cache = None

    for ins, val, ans in zip(instructions, values, answer):
        if ins == 'LRUCache':
            cache = cacheClass(*val)
            ret = None
        elif ins == 'put':
            ret = cache.put(*val)
        elif ins == 'get':
            ret = cache.get(*val)
        else:
            assert False

        assert ret == ans


def test_Naive():
    for test in testcase:
        helper(*test, Naive)


def test_OrderedDict():
    for test in testcase:
        helper(*test, OrderedDict)


def test_Queue():
    for test in testcase:
        helper(*test, Queue)


def test_DoubleLinkedList():
    for test in testcase:
        helper(*test, DoubleLinkedList)
