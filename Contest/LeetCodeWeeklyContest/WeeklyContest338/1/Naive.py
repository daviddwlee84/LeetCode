from typing import List

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        answer = 0
        
        if k >= numOnes:
            k -= numOnes
            answer = numOnes
        else:
            answer = k
            return answer
        

        if k >= numZeros:
            k -= numZeros
        else:
            return answer
        
        if k >= numNegOnes:
            answer -= numNegOnes
        else:
            answer -= k

        return answer
