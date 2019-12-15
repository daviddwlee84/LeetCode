import math
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        temp = "123456789"
        lowDigits = int(math.log10(low)) + 1
        highDigits = int(math.log10(high)) + 1

        ans = []
        while lowDigits < highDigits:
            window = lowDigits
            for i in range(len(temp) - window + 1):
                candidate = int(temp[i:i+window])
                if candidate < low:
                    continue
                ans.append(candidate)
            lowDigits += 1
        window = highDigits
        for i in range(len(temp) - window + 1):
            candidate = int(temp[i:i+window])
            if candidate > high:
                break
            if candidate < low:
                continue
            ans.append(candidate)
        return ans
