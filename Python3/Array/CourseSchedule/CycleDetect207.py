from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Problem becoming => if this graph is acyclic
        """
        self.neighbour = defaultdict(list)
        for start, end in prerequisites:
            self.neighbour[start].append(end)

        visited = [False] * numCourses
        recursion_stack = [False] * numCourses
        for course in range(numCourses):
            if not visited[course]:
                if self.isCycleExist(course, visited, recursion_stack):
                    return False
        return True

    def isCycleExist(self, course: int, visited: List[bool], recursion_stack: List[bool]) -> bool:
        """
        https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
        """

        visited[course] = True
        recursion_stack[course] = True
        for neighbour in self.neighbour[course]:
            if not visited[neighbour]:
                if self.isCycleExist(neighbour, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbour]:
                return True

        recursion_stack[course] = False
        return False

# Runtime: 124 ms, faster than 40.11% of Python3 online submissions for Course Schedule.
# Memory Usage: 15.8 MB, less than 53.75% of Python3 online submissions for Course Schedule.
