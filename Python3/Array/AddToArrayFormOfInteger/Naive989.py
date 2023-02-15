from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp = 0
        base = 10 ** (len(num) - 1)
        for n in num:
            temp += base * n
            base //= 10

        temp += k

        answer = []

        while temp > 0:
            answer.append(temp % 10)
            temp //= 10

        answer.reverse()
        return answer

# Better
# class Solution:
#     def addToArrayForm(self, num: List[int], k: int) -> List[int]:
#         i = len(num) - 1
#         new = []
#         carry = False
#         while k != 0 and i >= 0:
#             add = k % 10
#             k //= 10
#             s = num[i] + add + 1 if carry else num[i] + add
#             carry = s > 9
#             num[i] = s % 10
#             i -= 1
#         while carry and i >= 0:
#             s = num[i] + 1
#             carry = s > 9
#             num[i] = s % 10
#             i -= 1
#         if carry and i < 0:
#             carry = False
#             k += 1
#         while k != 0:
#             add = k % 10
#             k //= 10
#             new.append(add)
#         return list(reversed(new)) + num
