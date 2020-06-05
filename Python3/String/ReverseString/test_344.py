from Naive344 import Solution as naive
from Recursive344 import Solution as recursive

strings = [
    "hello",
    "Hannah"
    "A",
]


def test_naive():
    for string in strings:
        s = list(string)
        s_ori = s.copy()
        naive().reverseString(s)
        s_ori.reverse()
        assert s == s_ori


def test_recursive():
    for string in strings:
        s = list(string)
        s_ori = s.copy()
        recursive().reverseString(s)
        s_ori.reverse()
        assert s == s_ori
