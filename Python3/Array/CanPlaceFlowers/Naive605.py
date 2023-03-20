from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i - 1 < 0 or (i >= 0 and flowerbed[i - 1] != 1)) \
                        and (i + 1 >= len(flowerbed) or (i < len(flowerbed) and flowerbed[i + 1] != 1)):
                    flowerbed[i] = 1
                    n -= 1
            if n == 0:
                return True

        return False
