class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        bin_str = bin(num)[2:]
        if bin_str[0] == '1':
            if len(bin_str[1:]) % 2 == 0:
                if bin_str[1:] == '0' * len(bin_str[1:]):
                    return True
        return False

# class Solution:
#     def isPowerOfFour(self, num: int) -> bool:
#         if num == 0:
#             return False
#         return (num & num - 1 == 0) & len(bin(num)) % 2 == 1

# class Solution:
#     def isPowerOfFour(self, num):
#         if num <= 0:
#             return False
#         z = bin(num)[::-1]
#         if z.count('1') > 1:
#             return False
#         p = z.index('1')
#         return p % 2 == 0
