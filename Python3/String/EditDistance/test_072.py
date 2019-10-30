from DP072 import Solution as DP

testcase = [
    ("horse", "ros", 3),
    ("intention", "execution", 5),
    ("", "", 0),
    ("a", "a", 0),
    ("a", "", 1), # add
    ("ab", "a", 1), # delete
    ("a", "e", 1) # replace
]

def test_dp():
    for word1, word2, ans in testcase:
        assert DP().minDistance(word1, word2) == ans   
