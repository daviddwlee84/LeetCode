from TwoPointer015 import Solution as twoPointer
from Naive015 import Solution as Naive
from TwoPointer2_015 import Solution as twoPointer2
from BinarySearch015 import Solution as binarySearch

nums = []
nums.append([-1, 0, 1, 2, -1, -4])
nums.append([0, 0, 0, 0])
nums.append([3, 0, -2, -1, 1, 2])
nums.append([-12, 12, -5, -4, -12, 11, 9, -11, 13, 1, 12, -1, 8, 1, -9, -11, -13, -4, 10, -9, -6, -11, 1, -15, -3, 4, 0, -15, 3, 6, -4, 7, 3, -2, 10, -2, -6, 4, 2, -7, 12, -1, 7, 6, 7, 6, 2, 10, -13, -3, 8, -12, 2, -5, -12, 6, 6, -5,
             6, -5, -14, 9, 9, -4, -8, 4, 2, -7, -15, -11, -7, 12, -4, 8, -5, -12, -1, 12, 5, 1, -5, -1, 5, 12, 9, 0, 3, 0, 3, -14, 2, -4, 2, -4, 0, 1, 7, -13, 9, -1, 13, -12, -11, -6, 11, -1, -10, -5, -3, 10, 3, 7, -6, -15, -4, 10, 1, 14, -12])

ans = []
ans.append([[-1, 0, 1], [-1, -1, 2]])
ans.append([[0, 0, 0]])
ans.append([[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
ans.append([[-15, 1, 14], [-15, 2, 13], [-15, 3, 12], [-15, 4, 11], [-15, 5, 10], [-15, 6, 9], [-15, 7, 8], [-14, 0, 14], [-14, 1, 13], [-14, 2, 12], [-14, 3, 11], [-14, 4, 10], [-14, 5, 9], [-14, 6, 8], [-14, 7, 7], [-13, -1, 14], [-13, 0, 13], [-13, 1, 12], [-13, 2, 11], [-13, 3, 10], [-13, 4, 9], [-13, 5, 8], [-13, 6, 7], [-12, -2, 14], [-12, -1, 13], [-12, 0, 12], [-12, 1, 11], [-12, 2, 10], [-12, 3, 9], [-12, 4, 8], [-12, 5, 7], [-12, 6, 6], [-11, -3, 14], [-11, -2, 13], [-11, -1, 12], [-11, 0, 11], [-11, 1, 10], [-11, 2, 9], [-11, 3, 8], [-11, 4, 7], [-11, 5, 6], [-10, -4, 14], [-10, -3, 13], [-10, -2, 12], [-10, -1, 11], [-10, 0, 10], [-10, 1, 9], [-10, 2, 8], [-10, 3, 7], [-10, 4, 6], [-10, 5, 5], [-9, -5, 14], [-9, -4, 13], [-9, -3, 12], [-9, -2, 11], [-9, -1, 10], [-9, 0, 9],
            [-9, 1, 8], [-9, 2, 7], [-9, 3, 6], [-9, 4, 5], [-8, -6, 14], [-8, -5, 13], [-8, -4, 12], [-8, -3, 11], [-8, -2, 10], [-8, -1, 9], [-8, 0, 8], [-8, 1, 7], [-8, 2, 6], [-8, 3, 5], [-8, 4, 4], [-7, -7, 14], [-7, -6, 13], [-7, -5, 12], [-7, -4, 11], [-7, -3, 10], [-7, -2, 9], [-7, -1, 8], [-7, 0, 7], [-7, 1, 6], [-7, 2, 5], [-7, 3, 4], [-6, -6, 12], [-6, -5, 11], [-6, -4, 10], [-6, -3, 9], [-6, -2, 8], [-6, -1, 7], [-6, 0, 6], [-6, 1, 5], [-6, 2, 4], [-6, 3, 3], [-5, -5, 10], [-5, -4, 9], [-5, -3, 8], [-5, -2, 7], [-5, -1, 6], [-5, 0, 5], [-5, 1, 4], [-5, 2, 3], [-4, -4, 8], [-4, -3, 7], [-4, -2, 6], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-3, -3, 6], [-3, -2, 5], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -2, 4], [-2, -1, 3], [-2, 0, 2], [-2, 1, 1], [-1, -1, 2], [-1, 0, 1], [0, 0, 0]])


def test_twoPointer():
    for i, case in enumerate(nums):
        toCheck = sorted(twoPointer().threeSum(case))
        # print(case, twoPointer().threeSum(case), toCheck)
        assert toCheck == sorted(ans[i])


def test_Naive():
    for i, case in enumerate(nums):
        toCheck = sorted(Naive().threeSum(case))
        # print(case, Naive().threeSum(case), toCheck)
        assert toCheck == sorted(ans[i])


def test_twoPointer2():
    for i, case in enumerate(nums):
        toCheck = sorted(twoPointer2().threeSum(case.copy()))
        # print(case, twoPointer2().threeSum(case), toCheck)
        assert list(map(list, list(toCheck))) == sorted(ans[i])


def test_binarySearch():
    for i, case in enumerate(nums):
        toCheck = sorted(binarySearch().threeSum(case))
        print(case, binarySearch().threeSum(case), toCheck)
        assert list(sorted(map(sorted, toCheck))) == sorted(ans[i])
