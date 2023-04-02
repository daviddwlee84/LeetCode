from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff = sorted([(r1 - r2, i) for i, (r1, r2) in enumerate(zip(reward1, reward2))], reverse=True)
        mouse1 = set([i for _, i in diff[:k]])
        
        answer = 0
        for i in range(len(reward1)):
            if i in mouse1:
                answer += reward1[i]
            else:
                answer += reward2[i]
        return answer

