from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Problem becoming => is it possible to do a topological sort

        https://www.youtube.com/watch?v=0LjVxtLnNOk
        """
        courseNumAbleToTake = 0

        inDegree = [0] * numCourses

        # find out how many prerequisites each course has
        for pre_course, _ in prerequisites:
            inDegree[pre_course] += 1

        # add initial courses which have no prerequisites
        stack = []
        for course, degree in enumerate(inDegree):
            if degree == 0:
                stack.append(course)

        while stack:
            curr = stack.pop()  # i.e. taking that course
            courseNumAbleToTake += 1

            for pre_course, course in prerequisites:
                if course == curr:
                    inDegree[pre_course] -= 1
                    if inDegree[pre_course] == 0:
                        stack.append(pre_course)

        return courseNumAbleToTake == numCourses

# Runtime: 908 ms, faster than 7.67% of Python3 online submissions for Course Schedule.
# Memory Usage: 15.1 MB, less than 84.89% of Python3 online submissions for Course Schedule.
