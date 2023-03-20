from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        self.ans = 0
        # We can't simply use set because the nums can be duplicated
        curr_visit = [False] * 1001

        def dfs(idx: int):
            # print(idx, curr_visit)
            if idx == len(nums):
                self.ans += 1
                return

            if not (nums[idx] >= k and curr_visit[nums[idx] - k]):
                curr_visit[nums[idx]] = True
                dfs(idx + 1)
                curr_visit[nums[idx]] = False

            dfs(idx + 1)

        dfs(0)

        return self.ans - 1
