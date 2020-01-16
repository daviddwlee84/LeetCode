from collections import deque
from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


def adjacency_list_to_graph(adj_list: List[List[int]]) -> Node:
    """
        For simplicity sake, each node's value is the same as the node's index (1-indexed)
        [] => empty graph
        [[]] => graph with only one node Node(1) and no neighbor
    """

    nodes = [Node(i+1) for i in range(len(adj_list))]
    for i, neigh_vals in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j-1] for j in neigh_vals]

    if len(nodes) > 0:
        return nodes[0]
    else:
        return None


def is_same_graph(a: Node, b: Node):
    """ currently must start from same node """
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False

    a_visited = set()
    b_visited = set()
    if a.val != b.val:
        return False

    queue = deque([(a, b)])

    while queue:
        a, b = queue.pop()
        if a.val != b.val:
            return False

        a_visited.add(a)
        b_visited.add(b)

        a_neigh = sorted(a.neighbors, key=lambda x: x.val)
        b_neigh = sorted(b.neighbors, key=lambda x: x.val)

        for a_nei, b_nei in zip(a_neigh, b_neigh):
            if a_nei not in a_visited and b_nei not in b_visited:
                queue.appendleft((a_nei, b_nei))
            elif (a_nei not in a_visited) ^ (b_nei not in b_visited):
                return False

    return True


def _get_test_graph() -> Node:
    """ this is a undirected graph """
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.neighbors.append(b)
    b.neighbors.append(c)
    c.neighbors.append(d)
    d.neighbors.append(a)

    return a


if __name__ == "__main__":
    # test
    graphA = _get_test_graph()
    graphB = _get_test_graph()

    print(is_same_graph(graphA, graphB))
    print(is_same_graph(graphA, Node(87)))

    graphC = adjacency_list_to_graph([[2, 4], [1, 3], [2, 4], [1, 3]])

    print(is_same_graph(graphC, graphC))
