from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - 1
        score = 0
        recheck = 0
        for _ in range(k):
            if recheck > 0:
                if cardPoints[left + recheck] > cardPoints[right - recheck]:
                    left += recheck
                    recheck = 0
                    score += cardPoints[left]
                    left += 1
                elif cardPoints[left] < cardPoints[right - recheck]:
                    right -= recheck
                    recheck = 0
                    score += cardPoints[right]
                    right -= 1
                else:
                    score += cardPoints[left + recheck]
                    recheck += 1
            else:
                if cardPoints[left] > cardPoints[right]:
                    score += cardPoints[left]
                    left += 1
                elif cardPoints[left] < cardPoints[right]:
                    score += cardPoints[right]
                    right -= 1
                else:
                    score += cardPoints[left]
                    recheck += 1
        return score


# WA

if __name__ == "__main__":
    print(Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3))
    print(Solution().maxScore([11, 49, 100, 20, 86, 29, 72], 4))
