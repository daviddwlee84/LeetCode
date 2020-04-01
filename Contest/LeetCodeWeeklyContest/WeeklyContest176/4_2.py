from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        self.final = [1] * len(target)
        return self.bottomUp(target)

    def bottomUp(self, temp: List[int]) -> bool:
        """
        Track from the end. Try to recover the target back to self.final.
        """
        if temp == self.final:
            return True

        # Find the max number
        index_max = max(range(len(temp)), key=temp.__getitem__)

        # Calculate the original number at that position
        recovered = temp[index_max] - (sum(temp) - temp[index_max])
        if recovered < 1:
            return False

        # Looking for the next one
        temp[index_max] = recovered
        return self.bottomUp(temp)

# Testcase
# [1441, 1, 1101, 11, 1, 41, 2601, 1, 1, 1, 1]
