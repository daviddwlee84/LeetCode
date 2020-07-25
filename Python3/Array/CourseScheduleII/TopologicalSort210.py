from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edge = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for a, b in prerequisites:
            edge[a].append(b)
            inDegree[b] += 1

        result = []

        stack = []
        for i, degree in enumerate(inDegree):
            if degree == 0:
                stack.append(i)

        while stack:
            course = stack.pop()
            result.append(course)
            for neighbour in edge[course]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    stack.append(neighbour)

        if len(result) != numCourses:
            return []

        return reversed(result)

# Runtime: 104 ms, faster than 83.79% of Python3 online submissions for Course Schedule II.
# Memory Usage: 15 MB, less than 86.33% of Python3 online submissions for Course Schedule II.
