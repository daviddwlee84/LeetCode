from TwoPointer015 import Solution as twoPointer

nums = []
nums.append([-1, 0, 1, 2, -1, -4])
nums.append([0, 0, 0, 0])
nums.append([3, 0, -2, -1, 1, 2])

ans = []
ans.append([[-1, 0, 1], [-1, -1, 2]])
ans.append([[0, 0, 0]])
ans.append([[-2, -1, 3],[-2, 0, 2],[-1, 0, 1]])

def test_twoPointer():
    for i, case in enumerate(nums):
        toCheck = sorted(twoPointer().threeSum(case))
        print(case, twoPointer().threeSum(case), toCheck)
        assert toCheck == sorted(ans[i])