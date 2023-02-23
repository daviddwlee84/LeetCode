from Naive502 import Solution as Naive
from SortHeap502 import Solution as SortHeap
from SortHeapImprove502 import Solution as SortHeapImprove

testcases = [
    ({'k': 2,
      'w': 0,
      'profits': [1, 2, 3],
      'capital': [0, 1, 1],
      }, 4),
    ({'k': 3,
      'w': 0,
      'profits': [1, 2, 3],
      'capital': [0, 1, 2],
      }, 6),
    ({'k': 1,
      'w': 2,
      'profits': [1, 2, 3],
      'capital': [1, 1, 2],
      }, 5),
]


def test_Naive():
    for testcase, ans in testcases:
        assert Naive().findMaximizedCapital(**testcase) == ans


def test_SortHeap():
    for testcase, ans in testcases:
        assert SortHeap().findMaximizedCapital(**testcase) == ans


def test_SortHeapImprove():
    for testcase, ans in testcases:
        assert SortHeapImprove().findMaximizedCapital(**testcase) == ans
