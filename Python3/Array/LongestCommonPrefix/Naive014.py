class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ""

        if len(strs) == 0:
            return prefix

        shortestlen = min(map(len, strs))

        for i in range(shortestlen):
            temp = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != temp:
                    return prefix
            prefix += temp

        return prefix