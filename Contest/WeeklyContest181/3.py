from typing import List

gridDir = {
    1: [[0, 1], [0, -1]],
    2: [[1, 0], [-1, 0]],
    3: [[0, -1], [1, 0]],
    4: [[1, 0], [0, 1]],
    5: [[0, -1], [-1, 0]],
    6: [[-1, 0], [0, 1]]
}


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.grid = grid
        self.end = [len(grid)-1, len(grid[0])-1]
        self.ans = False
        self.dfs([0, 0], [], set())
        return self.ans

    def dfs(self, currPos: List[int], lastPos: List[int], visited) -> bool:
        visited.add(tuple(currPos))
        if currPos == self.end:
            self.ans = True
            return True

        roadDir = gridDir[self.grid[currPos[0]][currPos[1]]]

        possibleDir = []
        for road in roadDir:
            nextX = currPos[0] + road[0]
            nextY = currPos[1] + road[1]

            if 0 <= nextX <= self.end[0] and 0 <= nextY <= self.end[1]:
                if lastPos and lastPos == [nextX, nextY]:
                    continue
                if tuple([nextX, nextY]) in visited:
                    continue

                possibleDir.append([nextX, nextY])

        if possibleDir:
            for nextPos in possibleDir:
                if tuple(nextPos) not in visited and self.nextConnectToMe(currPos, nextPos):
                    self.dfs(nextPos, currPos, visited)

            # return any([self.dfs(nextPos, currPos, visited) for nextPos in possibleDir if self.nextConnectToMe(currPos, nextPos)])
        else:
            return False

    def nextConnectToMe(self, currPos: List[int], nextPos: List[int]) -> bool:
        roadDir = gridDir[self.grid[nextPos[0]][nextPos[1]]]
        for road in roadDir:
            currX = nextPos[0] + road[0]
            currY = nextPos[1] + road[1]
            if currPos == [currX, currY]:
                return True

        return False


if __name__ == "__main__":
    print(Solution().hasValidPath([[2, 4, 3], [6, 5, 2]]), True)
    print(Solution().hasValidPath([[1, 2, 1], [1, 2, 1]]), False)
    print(Solution().hasValidPath([[1, 1, 2]]), False)
    print(Solution().hasValidPath([[1, 1, 1, 1, 1, 1, 3]]), True)
    print(Solution().hasValidPath([[2], [2], [2], [2], [2], [2], [6]]), True)
    print(Solution().hasValidPath([[4, 1], [6, 1]]), True)
