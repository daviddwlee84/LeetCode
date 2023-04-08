# 133. Clone Graph

## Description

Given a reference of a node in a [connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph) undirected graph.

Return a [deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a val (`int`) and a list (`List[Node]`) of its neighbors.

```java
class Node {
    public int val;
    public List<Node> neighbors;
}
```

**Test case format**:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with `val = 1`, the second node with `val = 2`, and so on. The graph is represented in the test case using an adjacency list.

**Adjacency list** is a collection of unordered **lists** used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

**Example 1**:

![ex1](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)

```txt
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

**Example 2**:

![ex2](https://assets.leetcode.com/uploads/2020/01/07/graph.png)

```txt
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
```

**Example 3**:

```txt
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

**Example 4**:

![ex4](https://assets.leetcode.com/uploads/2020/01/07/graph-1.png)

```txt
Input: adjList = [[2],[1]]
Output: [[2],[1]]
```

**Constraints**:

* `1 <= Node.val <= 100`
* `Node.val` is unique for each node.
* Number of Nodes will not exceed 100.
* There is no repeated edges and no self-loops in the graph.
* The Graph is connected and all nodes can be visited starting from the given node.

## Solution

### Recursive

### DFS, Stack

### BFS, Queue

## Resources

* [Clone an Undirected Graph - GeeksforGeeks](https://www.geeksforgeeks.org/clone-an-undirected-graph/)
* [Python DFS short solution - LeetCode Discuss](https://leetcode.com/problems/clone-graph/discuss/42354/Python-DFS-short-solution)
* [Java recursive, iterative DFS, BFS solutions with explanation - LeetCode Discuss](https://leetcode.com/problems/clone-graph/discuss/199890/java-recursive-iterative-dfs-bfs-solutions-with-explanation)

## Fail

```py
from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        dummy_head = Node()
        
        visited = set([node])
        queue = deque([(node, dummy_head)])
        while queue:
            temp, parent = queue.pop()
            visited.add(temp)
            clone = Node(temp.val)
            parent.neighbors.append(clone)
            for neigh in temp.neighbors:
                if neigh not in visited:
                    queue.appendleft((neigh, clone))
        
        return dummy_head.neighbors[0]
```
