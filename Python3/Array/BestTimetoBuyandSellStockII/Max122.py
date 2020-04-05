from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_without_stock = 0
        best_with_stock = -float('inf')

        for price in prices:
            best_with_stock = max(best_with_stock, best_without_stock - price)
            best_without_stock = max(
                best_without_stock, best_with_stock + price)

        return best_without_stock
