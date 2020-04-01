from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorPrefix = [0]
        for num in arr:
            xorPrefix.append(xorPrefix[-1] ^ num)

        ans = []
        for L, R in queries:
            # the XOR property
            ans.append(xorPrefix[R+1] ^ xorPrefix[L])
        return ans