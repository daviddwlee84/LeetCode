class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """ https://leetcode.com/problems/remove-k-digits/discuss/629860/Java-or-C%2B%2B-or-Python3-or-easy-explanation """
        stack = []  # store the digits of the result
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                # if last digit of result greater than the current digit,
                # then we need to delete it to get smallest number
                k -= 1
                stack.pop()
            stack.append(digit)
        if k > 0:
            # if we haven't use all our K, we can just delete the rest K digits
            stack = stack[:-k]

        # remove the leading zeros
        return "".join(stack).lstrip("0") or "0"
