from GeneralizedTwoPointer018 import Solution as GeneralizedTwoPointer

Nums = []
Nums.append([1, 0, -1, 0, -2, 2])

targets = []
targets.append(0)

solution = []
solution.append(
    [
        [-1,  0, 0, 1],
        [-2, -1, 1, 2],
        [-2,  0, 0, 2]
    ]
)

def test_GeneralizedTwoPointer():
    for i, nums in enumerate(Nums):
        assert sorted(GeneralizedTwoPointer().fourSum(nums, targets[i])) == sorted(solution[i])
