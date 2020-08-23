from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/discuss/685390/JavaC%2B%2BPython-Stack-One-Pass
        """
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)

        return prices
