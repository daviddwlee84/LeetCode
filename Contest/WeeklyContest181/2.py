from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            divisor = None
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    if not divisor:
                        divisor = i
                    else:
                        divisor = None
                        break
            if divisor and divisor != num // divisor:
                answer += sum([1, divisor, num//divisor, num])

        return answer


# Input:
# [1,2,3,4,5,6,7,8,9,10]
# Output:
# 18
# Expected:
# 45

if __name__ == "__main__":
    print(Solution().sumFourDivisors([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 45)
