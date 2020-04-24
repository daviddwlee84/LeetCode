from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        score = 0
        for split in range(k + 1):
            # print(cardPoints[:split], cardPoints[-(k-split):])
            if k != split:
                score = max(sum(cardPoints[:split]) +
                            sum(cardPoints[-(k-split):]), score)
            else:
                score = max(sum(cardPoints[:split]), score)

        return score

# TLE
