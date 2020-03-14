from typing import List


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def listToInterval(lst: List[List[int]]) -> List[Interval]:
    return [Interval(start, end) for start, end in lst]
