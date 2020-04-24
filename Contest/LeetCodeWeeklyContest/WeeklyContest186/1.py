from collections import Counter


class Solution:
    def maxScore(self, s: str) -> int:
        answer = 0
        for split in range(1, len(s)):
            answer = max(Counter(s[:split])['0'] +
                         Counter(s[split:])['1'], answer)

        return answer
