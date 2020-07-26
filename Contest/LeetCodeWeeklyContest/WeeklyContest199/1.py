from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [None] * len(indices)

        for i, index in enumerate(indices):
            answer[index] = s[i]

        return ''.join(answer)
