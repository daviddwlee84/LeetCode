from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        f = []

        def dfs(curr_num: str):
            # print(curr_num, f)

            if not (len(curr_num) > 1 and curr_num[0] == '0') and len(f) >= 2 and int(curr_num) < 2**31 and int(curr_num) == f[-1] + f[-2]:
                # print(curr_num, f)
                f.append(int(curr_num))
                return True

            for l in range(1, len(curr_num)):
                # each piece must not have extra leading zeroes
                if curr_num[0] == '0' and l > 1:
                    return False

                if len(f) >= 2 and int(curr_num[:l]) != f[-1] + f[-2]:
                    continue
                else:
                    if int(curr_num[:l]) >= 2 ** 31:
                        continue

                    f.append(int(curr_num[:l]))
                    if dfs(curr_num[l:]):
                        return True
                    f.pop()
            return False
        dfs(num)
        return f
