from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        DFS
        """
        def dfs(i: int, piece_left: List[List[int]]) -> bool:
            if i == len(arr):
                return True

            for piece in piece_left:
                if arr[i:i + len(piece)] == piece:
                    piece_left.remove(piece)
                    found = dfs(i + len(piece), piece_left)
                    piece_left.append(piece)
                    if found:
                        return True

            return False

        return dfs(0, pieces)
