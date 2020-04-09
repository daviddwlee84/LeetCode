import itertools


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """ https://leetcode.com/problems/backspace-string-compare/solution/ """

        def F(S: str):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
