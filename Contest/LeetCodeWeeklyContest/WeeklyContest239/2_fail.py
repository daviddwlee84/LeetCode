from typing import List
from itertools import combinations


class Solution:
    def splitString(self, s: str) -> bool:
        for num in range(1, len(s)):
            # print(list(combinations(range(1, len(s)), num)))
            for way in combinations(range(1, len(s)), num):
                num_set = []
                s_temp = s
                prev = 0
                for cut in list(way) + [len(s)]:
                    # if not s_temp[:cut - prev]:
                    #     # BUG
                    #     continue

                    num_set.append(s_temp[:cut - prev])
                    s_temp = s_temp[cut - prev:]
                    prev = cut

                # if len(num_set) != num + 1:
                #     # BUG
                #     continue

                if self.isValid(num_set):
                    return True
        return False

    def removeLeadingZero(self, num_str: str) -> int:
        for i, c in enumerate(num_str):
            if c != '0':
                break

        num_str = num_str[i:]
        if not num_str:
            return 0

        return eval(num_str)

    def isValid(self, raw_num_set: List[str]) -> bool:
        num_set = list(map(self.removeLeadingZero, raw_num_set))
        # print(raw_num_set, num_set)
        prev = None
        for num in num_set:
            if prev is None:
                prev = num
            elif prev != num + 1:
                return False
            prev = num
        return True


if __name__ == '__main__':
    print(Solution().splitString('0090089'))
    print(Solution().splitString('050043'))
    print(Solution().splitString('10009998'))  # [3, 6, 8]

# TLE:
# "13121110987654321"
