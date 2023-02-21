from typing import List
import numpy as np


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return np.array(matrix).T.tolist()
