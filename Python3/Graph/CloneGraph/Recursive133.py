from Graph.GraphNodeModule import Node
from collections import deque


class Solution:
    """ https://leetcode.com/problems/clone-graph/discuss/473725/Python-3-recursive-solution-faster-than-99 """

    def cloneGraph(self, node: Node) -> Node:
        clones = {}

        if not node:
            return None

        def clone(n: Node):
            if n not in clones:
                clones[n] = Node(n.val)
                clones[n].neighbors = list(map(clone, n.neighbors))

            return clones[n]

        return clone(node)

# Runtime: 36 ms, faster than 72.48% of Python3 online submissions for Clone Graph.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Clone Graph.
