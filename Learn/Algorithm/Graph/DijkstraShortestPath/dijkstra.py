from typing import List, Set

class Graph():
    """
    https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

    TODO: calculate the path information by creating a parent array and update the parent array when distance is updated
    """

    def __init__(self, adjacency_matrix: List[List[int]]) -> None:
        assert len(adjacency_matrix) == len(adjacency_matrix[0]), 'adjacency matrix should be a square matrix of edge weight'
        self.graph = adjacency_matrix.copy()
        self.vertices_num = len(self.graph)
    
    def print_graph(self, distance_from_source: List[int]):
        print('Vertex \tDistance from Source')
        for node_id in range(self.vertices_num):
            print(node_id, '\t', distance_from_source[node_id])
        
    def min_distance_vertex(self, distance_from_source: List[int], shortest_path_tree_vertices: Set[int]) -> int:
        """
        Find the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree
        """
        
        minimum_distance = float('inf')

        for node_id in range(self.vertices_num):
            if node_id not in shortest_path_tree_vertices and distance_from_source[node_id] < minimum_distance:
                minimum_distance = distance_from_source[node_id]
                min_index = node_id
        
        return min_index

    def dijkstra_single_source_shortest_path_algorithm(self, source_vertex: int) -> List[int]:
        distance_from_source = [float('inf')] * self.vertices_num
        distance_from_source[source_vertex] = 0
        shortest_path_tree_vertices = set()

        for _ in range(self.vertices_num):
            min_distance_vertex = self.min_distance_vertex(distance_from_source, shortest_path_tree_vertices)
            shortest_path_tree_vertices.add(min_distance_vertex)

            for node_id in range(self.vertices_num):
                distance_from_min_distance_vertex_to_node = self.graph[min_distance_vertex][node_id]
                # Has edge, not in the tree, distance from source can be update (found shorter path)
                if distance_from_min_distance_vertex_to_node > 0 \
                    and node_id not in shortest_path_tree_vertices \
                    and distance_from_source[node_id] > distance_from_source[min_distance_vertex] + distance_from_min_distance_vertex_to_node:

                    distance_from_source[node_id] = distance_from_source[min_distance_vertex] + distance_from_min_distance_vertex_to_node
        
        return distance_from_source

if __name__ == '__main__':
    graph = Graph([
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ])

    source = 0

    print(f'Result of Source from {source} vertex:')
    graph.print_graph(graph.dijkstra_single_source_shortest_path_algorithm(source))
