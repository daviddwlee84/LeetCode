class Solution:
    def minOperations(self, n: int) -> int:
        # 3: [1, 3, 5] => 2
        # 5: [1, 3, 5, 7, 9] => 6
        # 6: [1, 3, 5, 7, 9, 11] => 9
        # 10 / 2 = 5
        # 6 / 2 = 3
        # 7 - 5 / 2 = 1
        last = (2 * (n-1)) + 1
        first = 1

        if n % 2 == 0:
            return int((((last - first) // 2) + 1) * (n / 2) / 2)
        else:
            return int((((last - first) // 2) + 0) * ((n + 1) / 2) / 2)
