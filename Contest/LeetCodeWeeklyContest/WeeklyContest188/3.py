from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        Tree is a trap
        Just calculate all needed edges and multiply by 2
        """
        needToReach = set(i for i, has in enumerate(hasApple) if has)

        if not needToReach:
            return 0

        reached = set()
        edge_table = {toi: fromi for fromi, toi in edges}

        edge_need = set()

        while needToReach != set([0]):
            # print(needToReach, reached, edge_need)
            temp = needToReach.copy()
            for node in temp:
                if node in edge_table:
                    # print(node)
                    # import ipdb
                    # ipdb.set_trace()
                    reached.add(node)
                    needToReach.remove(node)
                    needToReach.add(edge_table[node])
                    edge_need.add((node, edge_table[node]))

        return len(edge_need) * 2

# TLE
# 4
# [[0,1],[1,2],[0,3]]
# [true,true,true,true]
# Ans: 6


if __name__ == "__main__":
    print(Solution().minTime(
        4, [[0, 1], [1, 2], [0, 3]], [True, True, True, True]))
