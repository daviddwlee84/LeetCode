from collections import defaultdict


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        cnt = defaultdict(int)
        
        def dfs(s_left: str, count: dict):
            # print(s_left, count)
            if all(count[c] >= k for c in ['a', 'b', 'c']):
                return 0
            if not s_left:
                return -1
            left_count = count.copy()
            left_count[s_left[0]] += 1
            left_dest = dfs(s_left[1:], left_count)
            right_count = count.copy()
            right_count[s_left[-1]] += 1
            right_dest = dfs(s_left[:-1], right_count)
            if left_dest >= 0:
                left_dest += 1
            if right_dest >= 0:
                right_dest += 1
            if left_dest < 0 and right_dest < 0:
                return -1
            if left_dest < 0 or right_dest < 0:
                return max(left_dest, right_dest)
            return min(left_dest, right_dest)
        
        return dfs(s, cnt)