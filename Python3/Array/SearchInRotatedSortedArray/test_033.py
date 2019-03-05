from BinarySearch033 import Solution as BinarySearch

input_answer = [
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([3, 1], 1), 1)
]

def test_binarysearch():
    for ((nums, target), answer) in input_answer:
        assert BinarySearch().search(nums, target) == answer
