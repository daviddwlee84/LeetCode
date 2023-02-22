from typing import List, Tuple
from itertools import combinations
from collections import defaultdict
import heapq

class Graph():
    """
    https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
    """

    def __init__(self, adjacency_matrix: List[List[int]]) -> None:
        assert len(adjacency_matrix) == len(adjacency_matrix[0]), 'adjacency matrix should be a square matrix of edge weight'
        self.graph = adjacency_matrix.copy()
        self.vertices_num = len(self.graph)
        self.adjacency_vertices = defaultdict(list)
        for u, v in combinations(range(self.vertices_num), 2):
            if self.graph[u][v] == 0:
                continue
            self.adjacency_vertices[u].append((v, self.graph[u][v]))
            self.adjacency_vertices[v].append((u, self.graph[u][v]))
    
    def print_graph(self):
        print(f'Graph vertices: {self.vertices_num}')
        print('Graph distances between vertices:')
        for u, v in combinations(range(self.vertices_num), 2):
            if self.graph[u][v] > 0:
                print(f'{u} <--> {v}: {self.graph[u][v]}')
        print(self.adjacency_vertices)
    
    def print_answer(self, distance_from_source: List[int], parents: List[List[int]], source: int = None):
        if source:
            print(f'Result of Source from {source} vertex:')
        print('Vertex', 'Distance from Source', 'Parents', sep='\t')
        for node_id in range(self.vertices_num):
            print(node_id, distance_from_source[node_id], parents[node_id], sep='\t')
        
    def dijkstra_single_source_shortest_path_algorithm(self, source_vertex: int) -> List[int]:
        priority_queue = []
        heapq.heappush(priority_queue, (0, source_vertex))
        distance_from_source = [float('inf')] * self.vertices_num
        distance_from_source[source_vertex] = 0
        parents = [[] for _ in range(self.vertices_num)]

        while priority_queue:
            # the first vertex in queue is the minimum distance vertex
            distance_from_min_distance_vertex_to_node, min_distance_vertex = heapq.heappop(priority_queue)

            for adj_node, weight in self.adjacency_vertices[min_distance_vertex]:
                if distance_from_source[adj_node] > distance_from_source[min_distance_vertex] + weight:
                    distance_from_source[adj_node] = distance_from_source[min_distance_vertex] + weight
                    parents[adj_node] += parents[min_distance_vertex]
                    parents[adj_node].append(min_distance_vertex)
                    # Sorted by distance_from_source[adj_node]
                    heapq.heappush(priority_queue, (distance_from_source[adj_node], adj_node))
        
        return distance_from_source, parents

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

    graph.print_graph()

    source = 0
    graph.print_answer(*graph.dijkstra_single_source_shortest_path_algorithm(source), source)
