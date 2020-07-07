from typing import List
from collections import defaultdict


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89345/Easy-concept-with-PythonC%2B%2BJava-Solution
        """

        # obtain everyone's info (group of people)
        # key=height, value=k-value, index in original array
        peopledict = defaultdict(list)
        result = []

        for i, (h, k) in enumerate(people):
            peopledict[h].append((k, i))

        heights = sorted(peopledict.keys(), reverse=True)

        for height in heights:
            for h, i in sorted(peopledict[height]):
                result.insert(h, people[i])

        return result

# Runtime: 184 ms, faster than 30.13% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.2 MB, less than 42.65% of Python3 online submissions for Queue Reconstruction by Height.
