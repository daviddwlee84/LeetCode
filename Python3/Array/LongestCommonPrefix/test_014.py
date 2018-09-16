from Naive014 import Solution as naive

allstrs = []
allstrs.append(['flower', 'flow', 'flight'])
allstrs.append(['dog', 'racecar', 'car'])

ans = []
ans.append("fl")
ans.append("")

def test_naive():
    for i, strs in enumerate(allstrs):
        assert naive().longestCommonPrefix(strs) == ans[i]
    