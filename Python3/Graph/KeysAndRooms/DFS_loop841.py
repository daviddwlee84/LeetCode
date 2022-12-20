from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dfs = [0]
        visited = set(dfs)
        while dfs:
            room = dfs.pop()
            visited.add(room)
            for neighbor in rooms[room]:
                if neighbor not in visited:
                    dfs.append(neighbor)

        return len(visited) == len(rooms)
