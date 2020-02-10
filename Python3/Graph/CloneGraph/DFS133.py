from Graph.GraphNodeModule import Node


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node

        # create new root
        root = Node(node.val)
        # use stack to DFS through all the nodes
        stack = [node]
        # because "Node.val is unique for each node", use a hashmap to store each node
        # in order to check if a node has been visited
        nodes = {}
        nodes[node.val] = root

        while stack:
            top = stack.pop()

            for neighbor in top.neighbors:
                if neighbor.val not in nodes:
                    # for the nodes haven't been visited
                    stack.append(neighbor)
                    nodes[neighbor.val] = Node(neighbor.val)
                nodes[top.val].neighbors.append(nodes[neighbor.val])

        return root

# Runtime: 36 ms, faster than 72.06% of Python3 online submissions for Clone Graph.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Clone Graph.
