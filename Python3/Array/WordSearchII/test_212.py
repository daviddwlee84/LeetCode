from Naive212 import Solution as naive

testcase = [
    ([
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ], ["oath", "pea", "eat", "rain"], ["eat", "oath"]),
    ([["a", "a"]], ["a"], ["a"]),
    ([["a", "a"]], ["aaa"], []),
    ([
        ["a", "b"],
        ["a", "a"]
    ], ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"], ["aaa", "aaab", "aaba", "aba", "baa"])
]

large_case = ['large_case.txt']
for case in large_case:
    with open(case, 'r') as stream:
        testcase.append(tuple(eval(item) for item in stream.readlines()))

def test_naive():
    for board, words, ans in testcase:
        assert sorted(naive().findWords(board, words)) == sorted(ans)
