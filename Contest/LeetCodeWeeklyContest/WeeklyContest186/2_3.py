from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cumulative_left_k = [0]
        for i in range(k):
            cumulative_left_k.append(cardPoints[i] + cumulative_left_k[-1])
        cumulative_right_k = [0]
        for i in range(k):
            cumulative_right_k.append(
                cardPoints[-i-1] + cumulative_right_k[-1])

        score = 0

        for i in range(k + 1):
            score = max(
                score, cumulative_left_k[i] + cumulative_right_k[k - i])

        return score
