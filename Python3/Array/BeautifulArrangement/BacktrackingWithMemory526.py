class Solution:
    memo = {}

    def countArrangement(self, n: int) -> int:
        def count(i, X):
            if i < 2:
                return 1
            if X not in self.memo:
                self.memo[X] = sum(count(i - 1, X - {x})
                                   for x in X
                                   if x % i == 0 or i % x == 0)
            return self.memo[X]
        return count(n, frozenset(range(1, n + 1)))

# Runtime: 52 ms, faster than 96.68% of Python3 online submissions for Beautiful Arrangement.
# Memory Usage: 18.4 MB, less than 8.45% of Python3 online submissions for Beautiful Arrangement.
