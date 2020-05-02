class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        answer = 0
        for s in S:
            if s in jewels:
                answer += 1

        return answer

# Runtime: 32 ms, faster than 39.24% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 13.6 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.
