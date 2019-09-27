from HTHeap347 import Solution as HashTable

nums_k_ans = [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([1, 2], 2, [1, 2])
]


def test_HashTable():
    for nums, k, ans in nums_k_ans:
        assert HashTable().topKFrequent(nums, k) == ans
