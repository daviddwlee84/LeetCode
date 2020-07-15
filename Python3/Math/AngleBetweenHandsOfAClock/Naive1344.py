class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hours_in_minutes = (hour % 12 + minutes / 60) * 5
        diff = abs(hours_in_minutes - minutes)
        diff = min(60 - diff, diff)
        return diff * 6
