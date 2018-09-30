from Naive008 import Solution as naive

string = []
string.append("42")
string.append("   -42")
string.append("4193 with words")
string.append("words and 987")
string.append("-91283472332")
string.append("2147483648")

answer = []
answer.append(42)
answer.append(-42)
answer.append(4193)
answer.append(0)
answer.append(-2147483648)
answer.append(2147483647)

def test_naive():
    for i, s in enumerate(string):
        assert naive().myAtoi(s) == answer[i]