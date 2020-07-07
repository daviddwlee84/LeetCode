from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort%2BInsert-solution
        """
        people.sort(key=lambda p: (-p[0], p[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue

# Runtime: 164 ms, faster than 35.99% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.4 MB, less than 14.04% of Python3 online submissions for Queue Reconstruction by Height.
