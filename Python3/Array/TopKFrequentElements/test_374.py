from Naive347 import Solution as Naive
from HTHeap347 import Solution as HTHeap
from HTHeap2_347 import Solution as HTHeap2
from Quickselect347 import Solution as Quickselect
from BucketSort347 import Solution as BucketSort
from HT347 import Solution as HT

nums_k_ans = [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([1, 2], 2, [1, 2])
]


def test_Naive():
    for nums, k, ans in nums_k_ans:
        assert Naive().topKFrequent(nums, k) == ans


def test_HTHeap():
    for nums, k, ans in nums_k_ans:
        assert HTHeap().topKFrequent(nums, k) == ans


def test_HTHeap2():
    for nums, k, ans in nums_k_ans:
        assert HTHeap2().topKFrequent(nums, k) == ans


def test_Quickselect():
    for nums, k, ans in nums_k_ans:
        assert sorted(Quickselect().topKFrequent(nums, k)) == ans


def test_BucketSort():
    for nums, k, ans in nums_k_ans:
        assert sorted(BucketSort().topKFrequent(nums, k)) == ans


def test_HT():
    for nums, k, ans in nums_k_ans:
        assert sorted(HT().topKFrequent(nums, k)) == ans
