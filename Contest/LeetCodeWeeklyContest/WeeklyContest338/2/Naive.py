from typing import List
import re
import bisect


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n: int):
            return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

        primes = [x for x in range(1000) if is_prime(x)]

        # print(primes)

        prev = 0
        for num in nums:
            i = bisect.bisect_left(primes, num)
            # Error: [998,2]
            if i >= len(primes):
                i = len(primes) - 1

            while i >= 0 and num - primes[i] <= prev:
                i -= 1
                # print(primes[i])

            if i == -1 and num <= prev:
                return False

            if num <= primes[i]:
                if num > prev:
                    prev = num
                else:
                    return False
            else:
                prev = num - primes[i]

        return True

# WA (solved)
# [998,2]
# True

# WA (solved)
# [2,2]
# False

# TLE
# [2,14]
# ... True..?
