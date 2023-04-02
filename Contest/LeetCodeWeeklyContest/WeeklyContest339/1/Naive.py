
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros = 0
        ones = 0
        count_zero = True
        answer = 0
        for c in s:
            if count_zero:
                if c == '0':
                    zeros += 1
                else:
                    count_zero = False
                    ones = 1
            else:
                if c == '0':
                    # end of ones
                    answer = max(answer, min(ones, zeros) * 2)
                    count_zero = True
                    zeros = 1
                    ones = 0
                else:
                    ones += 1
            # print(c, zeros, ones)

        if not count_zero:
            answer = max(answer, min(ones, zeros) * 2)

        return answer
