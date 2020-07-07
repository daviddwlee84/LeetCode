class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        https://leetcode.com/problems/arranging-coins/solution/
        """
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            coins = (1 + mid) * mid // 2
            if coins == n:
                return mid
            elif coins < n:
                left = mid + 1
            else:
                right = mid - 1

        return right

# Runtime: 32 ms, faster than 86.95% of Python3 online submissions for Arranging Coins.
# Memory Usage: 13.7 MB, less than 79.66% of Python3 online submissions for Arranging Coins.

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         l, r = 0, n
#         while l <= r:
#             mid = (l + r) // 2
#             cost = (1 + mid) * mid // 2
#             if cost <= n:
#                 ans = mid
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return ans
