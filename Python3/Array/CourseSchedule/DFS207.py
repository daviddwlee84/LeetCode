from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation

        0 : node has not been visited
        -1: node is being visited, if we found a vertex marked as -1, then there is a ring
        1 : node has already visited (course taken)
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for pre_course, course in prerequisites:
            graph[pre_course].append(course)

        def dfs(course):
            if visited[course] == -1:
                return False

            if visited[course] == 1:
                # already taken the course
                return True

            visited[course] = -1  # visiting node

            for next_course in graph[course]:
                # try all the neighbour
                if not dfs(next_course):
                    return False

            # complete visiting, take the course successfully
            visited[course] = 1
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

# Runtime: 140 ms, faster than 34.48% of Python3 online submissions for Course Schedule.
# Memory Usage: 16.7 MB, less than 27.10% of Python3 online submissions for Course Schedule.
