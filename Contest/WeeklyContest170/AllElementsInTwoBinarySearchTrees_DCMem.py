from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        self.arr = arr
        self.memory = {(i, i): val for i, val in enumerate(arr)}
        ans = []
        for L, R in queries:
            ans.append(self.singleQuery(L, R))
        return ans

    def singleQuery(self, L, R):
        if self.memory.get((L, R)) is not None:
            return self.memory.get((L, R))

        if L == R:
            return self.arr[L]
        elif R - L == 1:
            self.memory[(L, R)] = self.arr[L] ^ self.arr[R]
            return self.arr[L] ^ self.arr[R]
        elif R - L == 2:
            self.memory[(L, R)] = self.arr[L] ^ self.arr[L+1] ^ self.arr[R]
            return self.arr[L] ^ self.arr[L+1] ^ self.arr[R]
        else:
            M = (R + L)//2
            self.memory[(L, R)] = self.singleQuery(
                L, M) ^ self.singleQuery(M+1, R)
            return self.memory[(L, R)]
