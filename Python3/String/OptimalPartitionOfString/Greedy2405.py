class Solution:
    def partitionString(self, s: str) -> int:
        curr = set()
        ans = 0
        for c in s:
            if c not in curr:
                curr.add(c)
            else:
                curr = set([c])
                ans += 1
        if curr:
            ans += 1
        return ans
