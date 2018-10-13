from DC010 import Solution as DivideAndConquer
from TopDownDP010 import Solution as TopDownDP
from BottomUpDP010 import Solution as BottomUpDP

ss = []
ss.append("aa")
ss.append("aa")
ss.append("ab")
ss.append("aab")
ss.append("mississippi")
ss.append("ab")
ss.append("aaa")
ss.append("aaa")
ss.append("a")
ss.append("a")
ss.append("a")
ss.append("ab")
ss.append("ab")
ss.append("aasdfasdfasdfasdfas")
ss.append("aaaaaaaaaaaaab")

ps = []
ps.append("a")
ps.append("a*")
ps.append(".*")
ps.append("c*a*b")
ps.append("mis*is*p*")
ps.append(".*c")
ps.append("a*a")
ps.append("aaaa")
ps.append("ab*")
ps.append("ab*a")
ps.append(".*..a*")
ps.append(".*..")
ps.append(".*..c*")
ps.append("aasdf.*asdf.*asdf.*asdf.*s")
ps.append("a*a*a*a*a*a*a*a*a*a*c")


ans = []
ans.append(False)
ans.append(True)
ans.append(True)
ans.append(True)
ans.append(False)
ans.append(False)
ans.append(True)
ans.append(False)
ans.append(True)
ans.append(False)
ans.append(False)
ans.append(True)
ans.append(True)
ans.append(True)
ans.append(False)

def test_DC():
    for i, s in enumerate(ss):
        assert DivideAndConquer().isMatch(s, ps[i]) == ans[i]

def test_TopDownDP():
    for i, s in enumerate(ss):
        assert TopDownDP().isMatch(s, ps[i]) == ans[i]

def test_BottomUpDP():
    for i, s in enumerate(ss):
        assert BottomUpDP().isMatch(s, ps[i]) == ans[i]