from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = float('inf')
        answer = 0

        for price in prices:
            if price < cur_min:
                cur_min = price

            answer = max(price - cur_min, answer)

        return answer
