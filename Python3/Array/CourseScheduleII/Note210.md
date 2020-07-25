# 210. Course Schedule II

## Description

There are a total of n courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

**Example 1**:

```txt
Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .
```

**Example 2**:

```txt
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
```

**Note**:

1. The input prerequisites is a graph represented by **a list of edges**, not adjacency matrices. Read more about how a graph is represented.
2. You may assume that there are no duplicate edges in the input prerequisites.

> Hint
>
> 1. This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
> 2. [Topological Sort via DFS](https://class.coursera.org/algo-003/lecture/52) - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
> 3. Topological sort could also be done via [BFS](http://en.wikipedia.org/wiki/Topological_sorting#Algorithms).

## Solution

### Topological Sort

---

Fail: thought it need to get all topological result but seems it just need any of them

(unfinished)

```py
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Find all topological sort result

        https://www.geeksforgeeks.org/all-topological-sorts-of-a-directed-acyclic-graph/
        """

        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for v, w, in prerequisites:
            adj[v].append(w)
            inDegree[w] += 1

        visited = [False] * numCourses
        result = []
        temp = []

        def allTopologicalSort():
            found_all = False

            for i in range(numCourses):
                # If in degree is 0 and not yet visited
                # then choose that vertex
                if inDegree[i] == 0 and not visited[i]:
                    # reducing indegree of adjacent vertices
                    for u in adj[i]:
                        inDegree[i] -= 1

                    # including in temp
                    temp.append(i)
                    visited[i] = True

                    # recursive call
                    allTopologicalSort()

                    # resetting visited, temp and in degree
                    visited[i] = False
                    temp.pop()

                    # reducing indegree of adjacent vertices
                    for u in adj[i]:
                        inDegree[i] += 1

                    found_all = True

            # We reach here if all vertices are visited
            if not found_all:
                result.append(temp.copy())

        allTopologicalSort()
        return result
```