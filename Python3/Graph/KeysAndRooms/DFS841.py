from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room: int):
            visited.add(room)
            # print(room, visited)
            for neighbor in rooms[room]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(0)
        return len(visited) == len(rooms)
