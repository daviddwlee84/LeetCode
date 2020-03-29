from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0

        answer = 0
        for i in range(len(rating)-2):
            j = i + 1
            while j < len(rating) - 1:
                k = j + 1
                while k < len(rating):
                    if rating[i] < rating[j] < rating[k] or rating[k] < rating[j] < rating[i]:
                        answer += 1
                    k += 1
                j += 1

        return answer
