from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        candidate = []
        for i, row in enumerate(mat):
            soldiers = 0
            for cell in row:
                if cell == 0:
                    break
                soldiers += 1

            candidate.append((i, soldiers))

        return [i for i, _ in sorted(candidate, key=lambda item: (item[1], item[0]))][:k]

# similar to https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/discuss/1066759/Python.-Super-simple-and-Easy-understanding-solution.
