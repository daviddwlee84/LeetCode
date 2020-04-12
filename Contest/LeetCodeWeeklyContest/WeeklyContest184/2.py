from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i + 1 for i in range(m)]
        answer = []
        for query in queries:
            index = P.index(query)
            answer.append(index)
            P.remove(query)
            P.insert(0, query)

        return answer
