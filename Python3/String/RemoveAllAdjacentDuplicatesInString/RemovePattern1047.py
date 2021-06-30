from string import ascii_lowercase


class Solution:
    def removeDuplicates(self, s: str) -> str:
        # ['aa', 'bb', ...]
        duplicates = [2 * ch for ch in ascii_lowercase]

        prev_length = -1

        # If string is not changing anymore
        while prev_length != len(s):
            prev_length = len(s)

            # Try to remove all the duplicates
            for d in duplicates:
                s = s.replace(d, '')

        return s

# Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.4 MB, less than 96.94% of Python3 online submissions for Remove All Adjacent Duplicates In String.


# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         for c in s:
#             if 2 * c in s:
#                 s = s.replace(2 * c, '')
#         return s
#
# Runtime: 2100 ms, faster than 5.01% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.2 MB, less than 99.85% of Python3 online submissions for Remove All Adjacent Duplicates In String.
