from collections import defaultdict


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        """
        https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/Python-Binary-search-O(n-log-n)-average-with-Rabin-Karp-explained
        """
        begin, end = 0, len(S)
        q = (1 << 31) - 1

        answer = ''

        while begin + 1 < end:
            mid = (begin + end) // 2
            found, candidate = self.RabinKarp(S, mid, q)
            if found:
                # update answer and try to find longer answer
                begin, answer = mid, candidate
            else:
                end = mid

        return answer

    def RabinKarp(self, S: str, M: int, q: int) -> bool:
        """
        Using rolling hash to hash the substring
        """
        if M == 0:
            # '' is substring of any string
            return True

        # auxiliary value for fast update of rolling hash
        h = (1 << (8 * M - 8)) % q
        # because it is more than ord('z') = 122
        d = 256
        t = 0

        # for each hash we keep start indexes of windows
        dic = defaultdict(list)

        # Evaluate hash for first window
        for i in range(M):
            t = (d * t + ord(S[i])) % q
        dic[t].append(i-M+1)

        # Evaluate hashes for all other windows in O(n), using evaluated h
        for i in range(len(S) - M):
            t = (d * (t - ord(S[i]) * h) + ord(S[i + M])) % q
            for j in dic[t]:
                # check all possible combinations and compare not hashes but original windows
                # to make sure that is was not a collision
                if S[i+1:i+M+1] == S[j:j+M]:
                    return (True, S[j:j+M])
            dic[t].append(i+1)

        return (False, '')

# Runtime: 2308 ms, faster than 29.48% of Python3 online submissions for Longest Duplicate Substring.
# Memory Usage: 40.1 MB, less than 25.11% of Python3 online submissions for Longest Duplicate Substring.
