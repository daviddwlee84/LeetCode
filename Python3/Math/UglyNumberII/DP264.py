class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        https://leetcode.com/problems/ugly-number-ii/discuss/69364/My-16ms-C%2B%2B-DP-solution-with-short-explanation
        https://leetcode.com/problems/ugly-number-ii/discuss/69384/My-expressive-Python-solution
        """
        # pointers for 2, 3, 5
        t2, t3, t5 = 0, 0, 0
        k = [1]
        for i in range(1, n):
            k.append(min(k[t2] * 2, k[t3] * 3, k[t5] * 5))
            if k[i] == k[t2] * 2:
                t2 += 1
            if k[i] == k[t3] * 3:
                t3 += 1
            if k[i] == k[t5] * 5:
                t5 += 1

        return k[-1]

# Runtime: 228 ms, faster than 40.92% of Python3 online submissions for Ugly Number II.
# Memory Usage: 13.9 MB, less than 53.88% of Python3 online submissions for Ugly Number II.
