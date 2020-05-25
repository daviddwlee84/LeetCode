from typing import List

class Solution:
    """ https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/discuss/651057/Python-by-O(-m*n-)-DP-w-Graph
    https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3340/discuss/651002/JAVA-Summary-of-4-different-solutions-or-Longest-Common-Subsequence
    """
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp_curr = [0] * (len(B) + 1)
        dp_prev = [0] * (len(B) + 1)

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp_curr[j] = dp_prev[j - 1] + 1
                else:
                    dp_curr[j] = max(dp_curr[j - 1], dp_prev[j])
            dp_prev, dp_curr = dp_curr, [0] * (len(B) + 1)
    
        return dp_prev[-1]