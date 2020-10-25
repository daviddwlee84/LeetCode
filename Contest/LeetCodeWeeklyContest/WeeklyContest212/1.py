from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        diff = 0
        last_release = 0
        answer = None
        for key, t in enumerate(releaseTimes):
            duration = t - last_release
            if duration > diff:
                diff = duration
                answer = keysPressed[key]
            elif duration == diff:
                answer = max(answer, keysPressed[key])
            last_release = t

        return answer
