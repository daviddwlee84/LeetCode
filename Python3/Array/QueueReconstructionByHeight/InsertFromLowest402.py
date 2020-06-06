from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        https://leetcode.com/problems/queue-reconstruction-by-height/discuss/673016/Python-Tired-of-inserting-from-the-tallest-Here-is-how-to-insert-from-the-lowest
        """
        people.sort()

        result = [None] * len(people)

        same_before = 0  # same height as the previous person
        for i, (height, count) in enumerate(people):
            if i > 0 and height == people[i - 1][0]:
                same_before += 1
            elif i > 0 and height != people[i - 1][0]:
                same_before = 0

            # find this person's correct position
            idx, empty = 0, 0
            while empty <= count - same_before:
                if result[idx] is None:
                    empty += 1
                idx += 1

            # insert the person
            result[idx - 1] = [height, count]

        return result

# Runtime: 732 ms, faster than 15.67% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.4 MB, less than 10.58% of Python3 online submissions for Queue Reconstruction by Height.
