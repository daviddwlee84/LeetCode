import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Directly calculate number in each position
        https://leetcode.com/problems/permutation-sequence/discuss/696390/Python-Math-solution-O(n2)-expained
        https://www.geeksforgeeks.org/factorial-in-python/
        """
        numbers = list(range(1, n + 1))
        answer = ''
        while n > 0:
            d = (k - 1) // math.factorial(n - 1)
            k -= d * math.factorial(n - 1)
            n -= 1
            answer += str(numbers[d])
            numbers.remove(numbers[d])

        return answer
