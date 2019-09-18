from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small = 0
        large = len(numbers)-1

        while large > small:
            if numbers[small] + numbers[large] > target:
                large -= 1
            elif numbers[small] + numbers[large] < target:
                small += 1
            else:
                break
        
        return [small+1, large+1]
