class Solution:
    def minOperations(self, n: int) -> int:
        # 3: [1, 3, 5] => 2
        # 5: [1, 3, 5, 7, 9] => 6
        # 6: [1, 3, 5, 7, 9, 11] => 9
        # 10 / 2 = 5
        # 6 / 2 = 3
        # 7 - 5 / 2 = 1
        last = (2 * (n-1)) + 1
        first = 1

        if n % 2 == 0:
            return int((((last - first) // 2) + 1) * (n / 2) / 2)
        else:
            return int((((last - first) // 2) + 0) * ((n + 1) / 2) / 2)


# class Solution:
#     def minOperations(self, n: int) -> int:
#         """
#         Alex Wice's Solution (with Math)

#         n   = [1 2 3 4 5 6 7  8  9]
#         ans = [0 1 2 4 6 9 12 16 20]

#         (This is how he "expore the O(1)" solution): map the function, expore each n, and find the "regular pattern"
#         """
#         m = n >> 1
#         ans = m * (m + 1)
#         if n % 2 == 0:
#             ans -= n >> 1
#         return ans


# class Solution:
#     def minOperations(self, n: int) -> int:
#         """
#         Alex Wice's Solution (with Math)

#         n   = [1 2 3 4 5 6 7  8  9]
#         ans = [0 1 2 4 6 9 12 16 20]
#         """
#         return (n // 2) * ((n + 1) // 2)
