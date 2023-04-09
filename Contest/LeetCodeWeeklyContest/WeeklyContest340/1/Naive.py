from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            if n % 2 == 0:
                return n == 2  # return False
            k = 3
            while k * k <= n:
                if n % k == 0:
                    return False
                k += 2
            return True
        ans = 0
        for i in range(len(nums)):
            if is_prime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if is_prime(nums[i][len(nums) - i - 1]):
                ans = max(ans, nums[i][len(nums) - i - 1])
        return ans
