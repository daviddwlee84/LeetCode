from typing import List
from functools import cmp_to_key


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/queue-reconstruction-by-height/discuss/672958/Problem-Explanation-or-Detailed-Steps-Solution-or-Simple-or-Using-Sorting

        Problem is to reconstruct the queue based on the height and K (K taller person can be in front of that person) value
        """

        people.sort(key=cmp_to_key(lambda p1, p2: p1[1] - p2[1]
                                   if p1[0] == p2[0] else p2[0] - p1[0]))

        answer = []

        for person in people:
            answer.insert(person[1], person)

        return answer

# Runtime: 116 ms, faster than 60.06% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.1 MB, less than 65.57% of Python3 online submissions for Queue Reconstruction by Height.
