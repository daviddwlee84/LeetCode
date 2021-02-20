class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parenthesis = {
            '(': 1,
            ')': -1
        }

        def balance(string: str, reverse=False):
            def update_count(char: str, count: int) -> int:
                return count + parenthesis.get(char, 0) * (-1)**reverse

            new_s = ''
            parentheses_count = 0

            if reverse:
                string = reversed(string)

            for c in string:
                # print(c, update_count(c, parentheses_count))
                if update_count(c, parentheses_count) < 0:
                    continue

                parentheses_count = update_count(c, parentheses_count)

                if reverse:
                    new_s = c + new_s
                else:
                    new_s += c

            return new_s, parentheses_count == 0

        s, finish = balance(s)
        # print(s)
        if not finish:
            s, _ = balance(s, reverse=True)
        return s

# Runtime: 896 ms, faster than 12.07% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 16.1 MB, less than 44.18% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.


if __name__ == '__main__':
    print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"), "lee(t(c)o)de")
    print(Solution().minRemoveToMakeValid("a)b(c)d"), "ab(c)d")
    print(Solution().minRemoveToMakeValid("))(("), "")
    print(Solution().minRemoveToMakeValid("(a(b(c)d)"), "a(b(c)d)")
