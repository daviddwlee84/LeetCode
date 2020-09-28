class Solution:

    def numDecodings(self, s: str) -> int:

        self.answer = 0

        mapping = {
            str(i + 1): chr(ord('A') + i) for i in range(26)
        }

        def dfs(s: str):
            if s == '':
                self.answer += 1
                return

            if len(s) >= 2 and s[:2] in mapping:
                dfs(s[2:])

            if s[:1] in mapping:
                dfs(s[1:])

        dfs(s)

        return self.answer

# from functools import lru_cache
#
#
# class Solution:
#
#     def numDecodings(self, s: str) -> int:
#
#         self.answer = 0
#
#         mapping = {
#             str(i + 1): chr(ord('A') + i) for i in range(26)
#         }
#
#         @lru_cache(None)
#         def dfs(s: str, cur_str: str):
#             if s == '':
#                 self.answer += 1
#                 return
#
#             if len(s) >= 2 and s[:2] in mapping:
#                 dfs(s[2:], cur_str + mapping[s[:2]])
#
#             if s[:1] in mapping:
#                 dfs(s[1:], cur_str + mapping[s[:1]])
#
#         dfs(s, '')
#
#         return self.answer

# TLE
#
# "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
# "9272971672512277354953939427689518239714228293463398742522722274929422229859968434281231132695842184"
