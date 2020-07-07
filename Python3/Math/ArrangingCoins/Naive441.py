class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = 0
        layer = 0
        while coins < n:
            layer += 1
            coins += layer

        if coins > n:
            layer -= 1

        return layer

# Runtime: 888 ms, faster than 42.18% of Python3 online submissions for Arranging Coins.
# Memory Usage: 13.8 MB, less than 76.20% of Python3 online submissions for Arranging Coins.
