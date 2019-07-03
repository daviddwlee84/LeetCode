from BinarySearch035 import Solution as bs

array = []
array.append([1, 3, 5, 6])
array.append([1, 3, 5, 6])
array.append([1, 3, 5, 6])
array.append([1, 3, 5, 6])

targets = []
targets.append(5)
targets.append(2)
targets.append(7)
targets.append(0)

positions = []
positions.append(2)
positions.append(1)
positions.append(4)
positions.append(0)


def test_binary_search():
    for nums, target, position in zip(array, targets, positions):
        assert bs().searchInsert(nums, target) == position
