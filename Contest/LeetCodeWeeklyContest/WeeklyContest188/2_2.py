from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xor = [0]
        for num in arr:
            xor.append(xor[-1] ^ num)
        print(xor)

        count = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    a = xor[i] ^ xor[j]
                    b = xor[j] ^ xor[k + 1]

                    # print(a, b, (i, j, k))

                    if a == b:
                        count += 1

        return count
