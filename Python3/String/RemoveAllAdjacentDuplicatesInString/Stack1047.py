class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
                continue

            stack.append(char)

        return ''.join(stack)

# Runtime: 72 ms, faster than 64.82% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.7 MB, less than 64.71% of Python3 online submissions for Remove All Adjacent Duplicates In String.


# Use `else` instead of `continue`
# Runtime: 64 ms, faster than 88.56% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.9 MB, less than 22.34% of Python3 online submissions for Remove All Adjacent Duplicates In String.
