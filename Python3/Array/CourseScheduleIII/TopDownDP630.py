from typing import List
from functools import lru_cache


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        It is always profitable to take the course with a smaller end day prior to a course with a larger end day. This is because, the course with a smaller duration, if can be taken, can surely be taken only if it is taken prior to a course with a larger end day.
        Based on this idea, firstly, we sort the given coursescourses array based on their end days. Then, we try to take the courses in a serial order from this sorted coursescourses array.

        https://leetcode.com/problems/course-schedule-iii/solution/

        TLE: https://leetcode.com/submissions/detail/488213148/testcase/
        """

        @lru_cache(None)
        def schedule(i: int, time: int):
            if i == len(courses):
                return 0

            taken = 0
            if time + courses[i][0] <= courses[i][1]:
                taken = 1 + schedule(i + 1, time + courses[i][0])

            not_taken = schedule(i + 1, time)

            return max(taken, not_taken)

        courses.sort(key=lambda x: x[1])

        return schedule(0, 0)
