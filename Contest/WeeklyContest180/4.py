from typing import List
from itertools import combinations  # at most k
import numpy as np


class Solution:
    """ brute force """

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        speed = np.array(speed)
        efficiency = np.array(efficiency)
        max_performance = 0
        for kk in range(1, k+1):
            for combination in combinations(list(range(n)), kk):
                performance = np.sum(speed[list(combination)]) * \
                    np.min(efficiency[list(combination)])
                performance %= 10e9+7
                max_performance = max(max_performance, performance)

        return int(max_performance)


if __name__ == "__main__":
    # print(Solution().maxPerformance(
    #     6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2), 60)
    print(Solution().maxPerformance(
        3, [2, 8, 2], [2, 7, 1], 2), 56)
