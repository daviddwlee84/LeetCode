from typing import List
import re
import bisect


class Solution:
    # primes = []

    # def __init__(self) -> None:
    #     def is_prime(n: int):
    #         return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None
    #     self.primes = [x for x in range(1000) if is_prime(x)]

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
              449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    def primeSubOperation(self, nums: List[int]) -> bool:

        # print('\n', nums)

        prev = 0
        for num in nums:
            if num <= prev:
                return False

            i = bisect.bisect_left(self.primes, num - prev) - 1

            # print(num, primes[i], prev)

            if i == -1:
                prev = num
            else:
                prev = num - self.primes[i]

        return True

# TLE
# 62 / 648 个通过测试用例
# [7,4,8,19,4]
# ... False..?

# TLE
# 63 / 648 个通过测试用例
# [2,14]
# ...

# Regular expression too slow...
