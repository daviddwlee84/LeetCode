#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self, s1: str, s2: str) -> str:
        """
        https://www.nowcoder.com/practice/6d29638c85bb4ffd80c020fe244baf11?tpId=196&tqId=37131&ru=/exam/oj
        """
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        if dp[len(s1)][len(s2)] == 0:
            return '-1'

        ans = ''
        i = len(s1)
        j = len(s2)

        while i >= 0 and j >= 0:
            if dp[i - 1][j] == dp[i][j - 1]:
                if dp[i - 1][j - 1] + 1 == dp[i][j]:
                    ans = s1[i - 1] + ans
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1

        return ans
