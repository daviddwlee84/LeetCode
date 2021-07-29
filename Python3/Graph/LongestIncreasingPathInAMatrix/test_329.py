from DFS329 import Solution as DFS

testcase = [
    ([[9,9,4],[6,6,8],[2,1,1]], 4),
    ([[3,4,5],[3,2,6],[2,2,1]], 4),
    ([[1]], 1),
]

def test_DFS():
    for matrix, ans in testcase:
        assert DFS().longestIncreasingPath(matrix) == ans
