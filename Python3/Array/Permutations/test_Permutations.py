from Backtracking046 import Solution as backtracking
from Recursive046 import Solution as recursive
from DFS046 import Solution as dfs
import itertools

testcase1 = [1, 2, 3]
answer1 = [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
testcase2 = []
answer2 = [[]]

answer1 = [list(x) for x in itertools.permutations(testcase1)]

def test_backtracking():
    assert sorted(backtracking().permute(testcase1)) == sorted(answer1)
    assert sorted(backtracking().permute(testcase2)) == sorted(answer2)

def test_recursive():
    assert sorted(recursive().permute(testcase1)) == sorted(answer1)
    assert sorted(recursive().permute(testcase2)) == sorted(answer2)

def test_dfs():
    assert sorted(dfs().permute(testcase1)) == sorted(answer1)
    assert sorted(dfs().permute(testcase2)) == sorted(answer2)