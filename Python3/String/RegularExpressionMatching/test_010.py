from DC010 import Solution as DivideAndConquer

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

def test_DC():
    for i, s in enumerate(ss):
        assert DivideAndConquer().isMatch(s, ps[i]) == ans[i]