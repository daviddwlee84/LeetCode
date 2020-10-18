from collections import defaultdict


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_indices = defaultdict(list)
        for i, c in enumerate(s):
            char_indices[c].append(i)

        answer = -1

        for indices in char_indices.values():
            if len(indices) < 2:
                continue

            answer = max(answer, indices[-1] - indices[0] - 1)

        return answer
