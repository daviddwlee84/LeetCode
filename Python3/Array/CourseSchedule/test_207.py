from CycleDetect207 import Solution as cycle_detect
from TopologicalSort207 import Solution as topological_sort
from DFS207 import Solution as dfs

testcase = [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False),
]


def test_cycle_detect():
    for numCourses, prerequisites, answer in testcase:
        assert cycle_detect().canFinish(numCourses, prerequisites) == answer


def test_topological_sort():
    for numCourses, prerequisites, answer in testcase:
        assert topological_sort().canFinish(numCourses, prerequisites) == answer


def test_dfs():
    for numCourses, prerequisites, answer in testcase:
        assert dfs().canFinish(numCourses, prerequisites) == answer
