from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(0, n):
            peak = 2 ** i
            for j in range(peak - 1, -1, -1):
                res.append(peak ^ res[j])
        return res


# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         ans = [0]
#         for i in range(n):
#             ans += [j + (1 << i) for j in ans[::-1]]
#         return ans


# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         i, N, gray = 1, 2**n, [0]
#         while i < N:
#             gray.extend(i + item for item in gray[::-1])
#             i *= 2
#         return gray
