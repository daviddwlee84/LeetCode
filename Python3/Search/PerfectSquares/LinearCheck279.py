class Solution:
    def numSquares(self, n: int) -> int:
        candidates = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]

        count = 0  # depth
        checking = {n}  # queue

        while checking:
            count += 1
            next_check = set()
            for x in checking:
                for square in candidates:
                    if x == square:
                        return count
                    elif x > square:
                        next_check.add(x - square)
                    else:
                        break
            checking = next_check

# class Solution:
#     def numSquares(self, n: int) -> int:
#         def is_divided_by(n, count):
#             if count == 1:
#                 return n in square_nums
#
#             for k in square_nums:
#                 if is_divided_by(n - k, count - 1):
#                     return True
#             return False
#
#         square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
#
#         for count in range(1, n+1):
#             if is_divided_by(n, count):
#                 return count
