from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        dist = 0
        i = startIndex
        while words[i] != target:
            i += 1
            if i >= len(words):
                i = 0
            if i == startIndex:
                return -1
            dist += 1

        dist2 = 0
        i = startIndex
        while words[i] != target:
            i -= 1
            if i < 0:
                i = len(words) - 1
            if i == startIndex:
                return -1
            dist2 += 1

        return min(dist, dist2)
