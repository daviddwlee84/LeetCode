from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        ans = 0
        min_salary = float('inf')
        max_salary = 0
        for money in salary:
            max_salary = max(max_salary, money)
            min_salary = min(min_salary, money)
            ans += money
        ans -= (max_salary + min_salary)

        return ans / (len(salary) - 2)

# class Solution:
#     def average(self, salary: List[int]) -> float:
#         return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)

# class Solution:
#     def average(self, salary: List[int]) -> float:
#         salary = sorted(salary)[1:-1]
#         return sum(salary) / len(salary)
