from Naive028 import Solution as naive

haystacks = []
haystacks.append("hello")
haystacks.append("aaaaa")
haystacks.append("")
haystacks.append("aaa")

needles = []
needles.append("ll")
needles.append("bba")
needles.append("")
haystacks.append("a")

answers = []
answers.append(2)
answers.append(-1)
answers.append(0)
answers.append(0)


def test_naive():
    for haystack, needle, answer in zip(haystacks, needles, answers):
        assert naive().strStr(haystack, needle) == answer
