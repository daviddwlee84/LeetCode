from TwoPointer016 import Solution as twoPointer

nums = []
nums.append([-1, 2, 1, -4])
nums.append([0, 1, 2])
nums.append([-3, -2, -5, 3, -4])
nums.append([4, 0, 5, -5, 3, 3, 0, -4, -5])

targets = []
targets.append(1)
targets.append(3)
targets.append(-1)
targets.append(-2)

ans = []
ans.append(2)
ans.append(3)
ans.append(-2)
ans.append(-2)

def test_twoPointer():
    for i in range(len(ans)):
        assert twoPointer().threeSumClosest(nums[i], targets[i]) == ans[i]
