class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        Alex Wice's Solution
        Brute Force

        a: increment => D
        b: rotate => N

        Time Complexity
        * worst O(N^2 D)
        """
        n = len(s)
        seen = set()
        A = list(map(int, s))
        for _ in range(10):
            for i in range(1, n, 2):
                A[i] += a
                A[i] %= 10
            seen.add(''.join(map(str, A)))

        for base in list(seen):
            for _ in range(n):
                base = base[b:] + base[:b]
                A = list(map(int, base))
                for _ in range(10):
                    for i in range(1, n, 2):
                        A[i] += a
                        A[i] %= 10
                    seen.add(''.join(map(str, A)))

        ans = min(seen)
        for c in seen:
            for _ in range(n):
                c = c[b:] + c[:b]
                ans = min(ans, c)

        return ans

# Runtime: 4252 ms, faster than 25.00% of Python3 online submissions for Lexicographically Smallest String After Applying Operations.
# Memory Usage: 15.3 MB, less than 25.00% of Python3 online submissions for Lexicographically Smallest String After Applying Operations.
