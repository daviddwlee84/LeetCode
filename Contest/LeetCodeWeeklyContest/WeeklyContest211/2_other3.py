class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        Alex Wice's Solution
        DFS
        """
        def neighbors(s: str):
            yield s[b:] + s[:b]
            A = list(map(int, s))
            for i in range(1, len(A), 2):
                A[i] += a
                A[i] %= 10
            yield ''.join(map(str, A))

        stack = [s]
        seen = {s}

        while stack:
            node = stack.pop()
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)

        return min(seen)

# Runtime: 2208 ms, faster than 50.00% of Python3 online submissions for Lexicographically Smallest String After Applying Operations.
# Memory Usage: 15.7 MB, less than 25.00% of Python3 online submissions for Lexicographically Smallest String After Applying Operations.
