from SlidingWindow003 import Solution as SlidingWindow
from SlidingWindowOptimized003 import Solution as SlidingWindowOptimized

strings = []
strings.append("abcabcbb")
strings.append("bbbbb")
strings.append("pwwkew")

answer = []
answer.append(3)
answer.append(1)
answer.append(3)


def test_slidingwindow():
    for i, s in enumerate(strings):
        assert SlidingWindow().lengthOfLongestSubstring(s) == answer[i]


def test_slidingwindowoptimized():
    for i, s in enumerate(strings):
        assert SlidingWindowOptimized().lengthOfLongestSubstring(s) == answer[i]