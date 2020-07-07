class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(bit == "1" for bit in bin(x ^ y)[2:])

# Runtime: 32 ms, faster than 50.95% of Python3 online submissions for Hamming Distance.
# Memory Usage: 14 MB, less than 5.44% of Python3 online submissions for Hamming Distance.

# Other
# https://leetcode.com/problems/hamming-distance/discuss/94697/Python-1-line-49ms

# https://en.wikipedia.org/wiki/Hamming_distance
# the symbols may be letters, bits, or digits, ...
