from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        # candidate square numbers that is less than n
        squaresToSearch = []
        x = 1
        while x*x <= n:
            squaresToSearch.append(x*x)
            x += 1
        
        queue = deque()
        queue.append(n)

        layer = 0
        # while the queue is not empty
        while len(queue) > 0:
            layer += 1

            for _ in range(len(queue)):
                toSearch = queue.popleft()
                
                for candidate in squaresToSearch:
                    if toSearch == candidate:
                        return layer
                    if toSearch < candidate:
                        break
                    queue.append(toSearch - candidate)
