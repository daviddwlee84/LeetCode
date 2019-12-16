from Backtracking093 import Solution as backtracking

testcase = [
    ("25525511135", ["255.255.11.135", "255.255.111.35"]),
    ("0000", ["0.0.0.0"]),
    ("255255255255", ["255.255.255.255"]),
    ("010010", ["0.10.0.10","0.100.1.0"]),
    ("103574606193", [])
]

def test_backtrack():
    for s, ans in testcase:
        assert set(backtracking().restoreIpAddresses(s)) == set(ans)
