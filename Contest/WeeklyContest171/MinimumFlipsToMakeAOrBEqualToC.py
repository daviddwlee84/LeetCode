class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]
        bin_c = bin(c)[2:]
        max_len = max(len(bin_a), len(bin_b), len(bin_c))
        if len(bin_a) < max_len:
            bin_a = '0' * (max_len - len(bin_a)) + bin_a
        if len(bin_b) < max_len:
            bin_b = '0' * (max_len - len(bin_b)) + bin_b
        if len(bin_c) < max_len:
            bin_c = '0' * (max_len - len(bin_c)) + bin_c
        ans = 0
        for i in range(len(bin_c)):
            if bin_c[i] == '1':
                if bin_a[i] == '0' and bin_b[i] == '0':
                    ans += 1
            else:
                little_sum = int(bin_a[i]) + int(bin_b[i])
                ans += little_sum
        return ans
