from itertools import permutations


class Solution:
    def countArrangement(self, n: int) -> int:
        ans = []
        for perm in permutations(range(1, n+1)):
            found = True
            for i, perm_i in enumerate(perm):
                if (i+1) % perm_i != 0 and perm_i % (i+1) != 0:
                    found = False
                    break
            if found:
                ans.append(perm)
        return len(ans)

# TLE at n = 11
