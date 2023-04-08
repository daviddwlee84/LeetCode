from Graph.GraphNodeModule import is_same_graph, adjacency_list_to_graph
from Graph.CloneGraph.Recursive133 import Solution as recursive
from Graph.CloneGraph.DFS133 import Solution as dfs
from Graph.CloneGraph.BFS133 import Solution as bfs

testcase = [
    adjacency_list_to_graph([[2, 4], [1, 3], [2, 4], [1, 3]]),
    adjacency_list_to_graph([[]]),
    adjacency_list_to_graph([]),
    adjacency_list_to_graph([[2], [1]])
]


def test_recursive():
    for graph in testcase:
        assert is_same_graph(recursive().cloneGraph(graph), graph)


def test_dfs():
    for graph in testcase:
        assert is_same_graph(dfs().cloneGraph(graph), graph)


def test_bfs():
    for graph in testcase:
        assert is_same_graph(bfs().cloneGraph(graph), graph)
