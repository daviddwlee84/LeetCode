from typing import List


class Solution:

    memory = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort()

        return self.tuple_helper(tuple(coins), amount)

    def tuple_helper(self, coins: tuple, amount: int) -> int:
        """
        Tried to do DP here...
        """
        if (coins, amount) in self.memory:
            return self.memory[(coins, amount)]

        if amount == 0:
            self.memory[(coins, amount)] = 0
            return 0

        if len(coins) < 1:
            self.memory[(coins, amount)] = -1
            return -1
        if len(coins) == 1:
            if amount % coins[0] != 0:
                self.memory[(coins, amount)] = -1
                return -1
            self.memory[(coins, amount)] = amount // coins[0]
            return amount // coins[0]

        if amount % coins[-1] == 0:
            self.memory[(coins, amount)] = amount // coins[-1]
            return amount // coins[-1]

        candidates = []
        for i in range(0, amount, coins[-1]):
            candidate = self.tuple_helper(coins[:-1], amount - i)
            if candidate != -1:
                candidates.append(candidate + i // coins[-1])

        if not candidates:
            self.memory[(coins, amount)] = -1
            return -1
        self.memory[(coins, amount)] = min(candidates)
        return min(candidates)

# WA (solved)
# [186,419,83,408]
# 6249

# TLE
# [438,86,218,138,358,152,129]
# 7656

# TLE
# [413,213,453,20,150,321,254,396,487,234]
# 5629

# TLE
# [77,82,84,80,398,286,40,136,162]
# 9794
