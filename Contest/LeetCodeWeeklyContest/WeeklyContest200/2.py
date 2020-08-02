from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = 0
        challenger = 1
        win_count = 0
        while win_count < k and challenger < len(arr):
            if arr[winner] < arr[challenger]:
                arr[winner], arr[challenger] = arr[challenger], arr[winner]
                win_count = 1
            else:
                win_count += 1
            challenger += 1

        return arr[winner]

# [1,25,35,42,68,70]
# 1
# 25
