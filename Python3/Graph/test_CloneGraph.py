from Graph.GraphNodeModule import is_same_graph, adjacency_list_to_graph
from Graph.CloneGraph.Recursive133 import Solution as recursive

testcase = [
    adjacency_list_to_graph([[2, 4], [1, 3], [2, 4], [1, 3]]),
    adjacency_list_to_graph([[]]),
    adjacency_list_to_graph([]),
    adjacency_list_to_graph([[2], [1]])
]


def test_recursive():
    for graph in testcase:
        assert is_same_graph(recursive().cloneGraph(graph), graph)
