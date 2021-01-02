from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        https://leetcode.com/problems/check-array-formation-through-concatenation/discuss/918408/Python-5-lines-hashmap
        """
        first_item_to_piece = {piece[0]: piece for piece in pieces}
        concat = []
        for num in arr:
            concat += first_item_to_piece.get(num, [])

        return arr == concat