from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        answer = 0
        for i in range(len(light)):
            if i == 0:
                sorted_bulb = [light[i]]
            else:
                # similar with insertion sort
                # but we don't need to actually sort the list
                # just make sure the most left and most right one are the smallest and biggest number
                if light[i] < sorted_bulb[0]:
                    sorted_bulb.insert(0, light[i])
                elif light[i] > sorted_bulb[-1]:
                    sorted_bulb.append(light[i])
                else:
                    # randomly insert in middle
                    sorted_bulb.insert(1, light[i])
            if sorted_bulb[0] == 1 and sorted_bulb[-1] == i + 1:
                answer += 1

        return answer

# pass
