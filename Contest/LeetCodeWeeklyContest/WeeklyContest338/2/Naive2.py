from typing import List
import re
import bisect


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n: int):
            return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

        primes = [x for x in range(1000) if is_prime(x)]

        prev = 0
        for num in nums:
            i = bisect.bisect_left(primes, num)
            found = False
            for prime in reversed(primes[:i]):
                if num - prime > prev:
                    found = True
                    break

            if found:
                prev = num - prime
            else:
                if num <= prev:
                    return False
                else:
                    prev = num

        return True

# TLE
# [7,4,8,19,4]
# ... False..?
