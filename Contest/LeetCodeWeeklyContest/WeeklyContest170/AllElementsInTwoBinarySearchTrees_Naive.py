from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        for L, R in queries:
            temp = 0
            for i in range(L, R+1):
                temp ^= arr[i]
            ans.append(temp)
        return ans
