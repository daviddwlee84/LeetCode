from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        def dfs(curr_digits: str):
            if low <= int(curr_digits) <= high:
                ans.append(int(curr_digits))
            elif int(curr_digits) > high:
                return

            if int(curr_digits[-1]) + 1 <= 9:
                curr_digits += str(int(curr_digits[-1]) + 1)
                dfs(curr_digits)

        for i in range(1, 10):
            dfs(str(i))

        return sorted(ans)
