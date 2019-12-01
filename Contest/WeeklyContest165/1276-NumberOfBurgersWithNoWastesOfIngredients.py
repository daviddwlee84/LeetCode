from typing import List
import numpy as np

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        a = np.array([[4, 2], [1, 1]])
        b = np.array([tomatoSlices, cheeseSlices])
        ans = np.linalg.solve(a, b)
        if ans[0] >= 0 and ans[1] >= 0 and int(ans[0]) == ans[0] and int(ans[1]) == ans[1]:
            return list(ans.astype(int))
        else:
            return []
 
if __name__ == "__main__":
    print(Solution().numOfBurgers(16, 7)) # [1,6]
    print(Solution().numOfBurgers(17, 4)) # []
    print(Solution().numOfBurgers(4, 17)) # []
    print(Solution().numOfBurgers(0, 0)) # [0,0]
    print(Solution().numOfBurgers(2, 1)) # [0,1]
