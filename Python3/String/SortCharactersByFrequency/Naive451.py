from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        answer = ''
        for char, count in sorted(Counter(s).items(), key=lambda x: x[1], reverse=True):
            answer += char * count

        return answer

# Runtime: 32 ms, faster than 95.39% of Python3 online submissions for Sort Characters By Frequency.
# Memory Usage: 15.3 MB, less than 7.14% of Python3 online submissions for Sort Characters By Frequency.
# other Pythonic solution
# https://leetcode.com/problems/sort-characters-by-frequency/discuss/645057/Python-3-today's-one-liner
