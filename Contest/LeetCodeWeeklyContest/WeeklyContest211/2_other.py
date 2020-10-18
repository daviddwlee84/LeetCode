import math


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        Alex Wice's Solution
        Best

        a: increment => D
        b: rotate => N

        Time Complexity:

        * worst O(N^2 D)

        > Ad hoc problem?!
        > https://stackoverflow.com/questions/1786735/what-is-exact-meaning-of-ad-hoc-in-programming
        """

        n = len(s)
        rotations = set()
        # for each possible rotation (O(n))
        for _ in range(n // math.gcd(len(s), b)):
            s = s[b:] + s[:b]
            rotations.add(s)

        ans = min(rotations)
        # O(1)
        for base in rotations:
            A = list(map(int, base))
            shift0 = 0
            if b & 1:
                shift0 = min(range(10), key=lambda i: (
                    int(base[0]) + i * a) % 10)

                for i in range(0, n, 2):
                    A[i] += shift0 * a
                    A[i] %= 10

            shift1 = min(range(10), key=lambda i: (int(base[1]) + i * a) % 10)
            for i in range(1, n, 2):
                A[i] += shift1 * a
                A[i] %= 10

            ans = min(ans, ''.join(map(str, A)))

        return ans

# Runtime: 76 ms, faster than 100.00% of Python3 online submissions for Lexicographically Smallest String After Applying Operations.
# Memory Usage: 14.2 MB, less than 25.00% of Python3 online submissions for Lexicographically Smallest String After Applying Operations.
