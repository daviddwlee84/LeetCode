class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            # https://www.geeksforgeeks.org/check-if-a-number-is-odd-or-even-using-bitwise-operators/
            if num & 1:
                # odd
                num -= 1
            else:
                # even
                num >>= 1
            steps += 1
        return steps
