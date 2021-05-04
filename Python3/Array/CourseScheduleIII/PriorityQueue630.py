from typing import List
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        By default heapq is min-heap, so we use negative course_duration

        https://leetcode.com/problems/course-schedule-iii/solution/
        """
        courses.sort(key=lambda x: x[1])
        queue = []

        time = 0

        for course_duration, course_end in courses:
            if time + course_duration <= course_end:
                heapq.heappush(queue, -course_duration)
                time += course_duration
            elif queue and -queue[0] > course_duration:
                time += course_duration + heapq.heappop(queue)
                heapq.heappush(queue, -course_duration)

        return len(queue)
