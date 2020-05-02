from collections import defaultdict

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stones_count = defaultdict(int)
        answer = 0
        for s in S:
            stones_count[s] += 1

        for j in J:
            answer += stones_count[j]

        return answer

# Runtime: 32 ms, faster than 39.24% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 13.8 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.
