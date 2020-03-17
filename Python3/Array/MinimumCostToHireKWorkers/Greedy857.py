from typing import List
from fractions import Fraction


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        minCost = float('inf')

        N = len(quality)

        # for each "captain" worker (the worker that will be paid their minimum wage expectation)
        for captain in range(N):
            # Must pay at least wage[captain] / quality[captain] per quality
            factor = Fraction(wage[captain], quality[captain])
            prices = []
            for worker in range(N):
                price = factor * quality[worker]
                if price < wage[worker]:
                    # we can't afford to hire this guy
                    continue
                prices.append(price)

            if len(prices) < K:
                # didn't hire enough employee
                continue

            # Hire K employee with the lowest prices
            prices.sort()
            minCost = min(minCost, sum(prices[:K]))

        return minCost
