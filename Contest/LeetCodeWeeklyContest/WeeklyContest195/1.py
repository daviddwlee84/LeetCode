class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0, 0)])
        curr_pos = (0, 0)
        for direction in path:

            if direction == 'N':
                curr_pos = (curr_pos[0] + 1, curr_pos[1])
            elif direction == 'E':
                curr_pos = (curr_pos[0], curr_pos[1] + 1)
            elif direction == 'S':
                curr_pos = (curr_pos[0] - 1, curr_pos[1])
            elif direction == 'W':
                curr_pos = (curr_pos[0], curr_pos[1] - 1)
        
            if curr_pos in visited:
                return True
            else:
                visited.add(curr_pos)
        
        return False