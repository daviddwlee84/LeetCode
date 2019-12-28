from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            ans.append([])
            for j in range(i+1):
                ans[i].append(self.C(i, j))
        return ans
        
    def C(self, m: int, n: int) -> int:
        assert m >= n
        return int(self.power(m)/(self.power(m-n) * self.power(n)))
        
    def power(self, n: int):
        assert n >= 0
        num = 1
        for i in range(1, n+1):
            num *= i
        return num

# Runtime: 32 ms, faster than 60.03% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.
