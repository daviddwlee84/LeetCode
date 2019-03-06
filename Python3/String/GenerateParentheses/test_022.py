from Backtracking022 import Solution as Backtracking

ns = []
ns.append(3)

answer = []
answer.append([
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
])

def test_backtracking():
    for i, n in enumerate(ns):
        assert sorted(Backtracking().generateParenthesis(n)) == sorted(answer[i])
