from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        same_color = 0
        color = [0] * n
        ans = []
        for i, c in queries:
            minus = 0
            plus = 0
            if color[i] != 0:
                if i > 0 and color[i] == color[i - 1]:
                    minus += 1
                if i < n - 1 and color[i] == color[i + 1]:
                    minus += 1

            color[i] = c

            if i > 0 and c == color[i - 1]:
                plus += 1
            if i < n - 1 and c == color[i + 1]:
                plus += 1

            same_color += plus - minus
            ans.append(same_color)

        return ans
