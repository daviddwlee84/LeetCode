from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        start = 0
        end = len(people) - 1

        answer = 0
        while start <= end:
            if people[end] + people[start] > limit:
                # Can only pick the heaviest one
                answer += 1
                end -= 1
            else:
                # Pick two people (heaviest one and another one (lightest))
                answer += 1
                start += 1
                end -= 1

        return answer
