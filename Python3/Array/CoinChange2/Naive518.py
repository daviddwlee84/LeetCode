from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.amount = amount
        self.coins = coins
        self.candidate = []
        self.backtracking(amount, tuple([0] * len(coins)))

        return len(self.candidate)

    @lru_cache(None)
    def backtracking(self, amount_left: int, curr_coins: List[int]):
        if amount_left == 0:
            self.candidate.append(curr_coins)

        for i, coin in enumerate(self.coins):
            if coin <= amount_left:
                next_coins = list(curr_coins)
                next_coins[i] += 1
                self.backtracking(amount_left - coin, tuple(next_coins))

        return

# TLE
