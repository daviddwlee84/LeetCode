from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        array = []
        answer = []
        for i in range(1, n + 1):
            array.append(i)
            answer.append('Push')
            if array == target:
                return answer

            if i not in target:
                array.pop()
                answer.append('Pop')
