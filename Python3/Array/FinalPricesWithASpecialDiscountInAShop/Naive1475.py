from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break

        return prices

# Runtime: 88 ms, faster than 22.16% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
# Memory Usage: 13.8 MB, less than 82.49% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
