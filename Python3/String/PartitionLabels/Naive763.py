from typing import List
from collections import Counter


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_pos_dict = {
            char: S.rindex(char)
            for char in S
        }
        left_most = 0
        answer = []
        while left_most < len(S):
            char = S[left_most]
            right_most = last_pos_dict[char]
            i = left_most + 1
            while i < right_most:
                right_most = max(right_most, last_pos_dict[S[i]])
                i += 1
            answer.append(right_most - left_most + 1)
            left_most = right_most + 1

        return answer

# Runtime: 48 ms, faster than 47.79% of Python3 online submissions for Partition Labels.
# Memory Usage: 13.8 MB, less than 57.92% of Python3 online submissions for Partition Labels.
