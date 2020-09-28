from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.n = n
        result = 0
        for num in reversed(range(1, 2**len(requests))):
            query = []
            i = 0
            while num:
                if num & 1:
                    query.append(requests[i])
                num >>= 1
                i += 1

            if len(query) > result and self.isBalance(*self.getInOutDegrees(query)):
                result = max(result, len(query))
        return result

    def getInOutDegrees(self, requests: List[List[int]]):
        inDegree = [0] * self.n
        outDegree = [0] * self.n

        for request in requests:
            outDegree[request[0]] += 1
            inDegree[request[1]] += 1

        return inDegree, outDegree

    def isBalance(self, inDegrees: List[int], outDegrees: List[int]) -> bool:
        for i in range(self.n):
            if inDegrees[i] != outDegrees[i]:
                return False
        return True
