from typing import List

LEFT = 0
RIGHT = 1


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_shift = self.combineShifts(shift)
        # because if shift over len(s) means it has round to start
        left_shift %= len(s)

        if left_shift < 0:
            # this seems can be remove, since python support negative index
            left_shift = len(s) - left_shift

        return s[left_shift:] + s[:left_shift]

    def combineShifts(self, shifts: List[List[int]]) -> int:
        """ count total left shift times, because left shift cancels the right shift """
        left_shift = 0
        for direction, times in shifts:
            if direction == LEFT:
                left_shift += times
            elif direction == RIGHT:
                left_shift -= times

        return left_shift
