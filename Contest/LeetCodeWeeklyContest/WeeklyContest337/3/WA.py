from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            print(nums)
            return 1

        this_is_beautiful = True
        for num in nums:
            for num2 in nums:
                if abs(num - num2) == k:
                    this_is_beautiful = False
                    break
            if not this_is_beautiful:
                break

        if this_is_beautiful:
            print(nums)

        answer = 0
        answer += this_is_beautiful
        for i in range(len(nums)):
            answer += self.beautifulSubsets(nums[:i] + nums[i + 1:], k)
            print(nums[:i] + nums[i + 1:])
        return answer


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        visited = set()

        def permutation(nums: List[int], k: int) -> int:

            if tuple(nums) in visited:
                return 0

            visited.add(tuple(nums))

            if len(nums) == 1:
                return 1

            this_is_beautiful = True
            for num in nums:
                for num2 in nums:
                    if abs(num - num2) == k:
                        this_is_beautiful = False
                        break
                if not this_is_beautiful:
                    break

            if this_is_beautiful:
                print(nums)

            answer = 0
            answer += this_is_beautiful
            for i in range(len(nums)):
                answer += self.beautifulSubsets(nums[:i] + nums[i + 1:], k)
                print(nums[:i] + nums[i + 1:])
            return answer

        return permutation(nums, k)
