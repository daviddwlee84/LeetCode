from itertools import tee


def pairwise(iterable):
    """
    https://docs.python.org/3/library/itertools.html#itertools-recipes
    https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list
    """
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def fill_section(start, end, array):
            # Transform for case of two end
            if start < 0:
                start = -end
            if end >= len(s):
                end = len(s) + (len(s) - start) - 1
            i = -1
            while start < end:
                i += 1
                if start >= 0:
                    array[start] += i
                if end < len(s):
                    array[end] += i
                start += 1
                end -= 1

            # odd section
            if start == end:
                i += 1
                array[start] += i

        ranges = []
        for i, char in enumerate(s):
            if char == c:
                ranges += [i]
        ranges = [-1] + ranges + [len(s)]

        answer = [0] * len(s)
        for start, end in pairwise(ranges):
            fill_section(start, end, answer)

        return answer
