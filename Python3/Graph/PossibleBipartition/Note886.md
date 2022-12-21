# 886. Possible Bipartition

## Description

We want to split a group of n people (labeled from `1` to `n`) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer `n` and the array `dislikes` where `dislikes[i] = [ai, bi]` indicates that the person labeled `ai` does not like the person labeled `bi`, return `true` *if it is possible to split everyone into two groups in this way*.

 
Example 1:

```txt
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
```

Example 2:

```txt
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
```

Example 3:

```txt
Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
```

**Constraints**:

* `1 <= n <= 2000`
* `0 <= dislikes.length <= 104`
* `dislikes[i].length == 2`
* `1 <= dislikes[i][j] <= n`
* `ai < bi`
* All the pairs of `dislikes` are unique.

## Solution

* [Official Solution - Possible Bipartition - LeetCode](https://leetcode.com/problems/possible-bipartition/solutions/2834180/possible-bipartition/)
* This problem is equivalent to determine if this graph is a [bipartite graph](https://en.wikipedia.org/wiki/Bipartite_graph).

## Failed

```py
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1:
            return True

        like_graph = [
            set(i for i in range(n) if i != j) for j in range(n)
        ]
        for a, b in dislikes:
            # shift to 0 to n - 1
            like_graph[a - 1].remove(b - 1)
            like_graph[b - 1].remove(a - 1)
        
        total = set(range(n))
        group_a = set()
        group_b = set()
        visited = set()

        def group_by_dfs(person: int, group: set):
            # print(person)
            visited.add(person)
            group.add(person)
            for like in like_graph[person]:
                if like not in visited:
                    if all(like in like_graph[m] for m in group):
                        group_by_dfs(like, group)
        
        # print(like_graph)

        group_by_dfs(0, group_a)
        print(group_a)
        
        if len(visited) == n:
            # only one group
            return False

        # left = total - visited
        left = total - group_a
        # print(total, visited, left)
        
        group_by_dfs(min(left), group_b)
        print(group_b)

        print(total - group_a - group_b)

        return len(visited) == n
```

Can't pass `(50, [[21,47],[4,41],[2,41],[36,42],[32,45],[26,28],[32,44],[5,41],[29,44],[10,46],[1,6],[7,42],[46,49],[17,46],[32,35],[11,48],[37,48],[37,43],[8,41],[16,22],[41,43],[11,27],[22,44],[22,28],[18,37],[5,11],[18,46],[22,48],[1,17],[2,32],[21,37],[7,22],[23,41],[30,39],[6,41],[10,22],[36,41],[22,25],[1,12],[2,11],[45,46],[2,22],[1,38],[47,50],[11,15],[2,37],[1,43],[30,45],[4,32],[28,37],[1,21],[23,37],[5,37],[29,40],[6,42],[3,11],[40,42],[26,49],[41,50],[13,41],[20,47],[15,26],[47,49],[5,30],[4,42],[10,30],[6,29],[20,42],[4,37],[28,42],[1,16],[8,32],[16,29],[31,47],[15,47],[1,5],[7,37],[14,47],[30,48],[1,10],[26,43],[15,46],[42,45],[18,42],[25,42],[38,41],[32,39],[6,30],[29,33],[34,37],[26,38],[3,22],[18,47],[42,48],[22,49],[26,34],[22,36],[29,36],[11,25],[41,44],[6,46],[13,22],[11,16],[10,37],[42,43],[12,32],[1,48],[26,40],[22,50],[17,26],[4,22],[11,14],[26,39],[7,11],[23,26],[1,20],[32,33],[30,33],[1,25],[2,30],[2,46],[26,45],[47,48],[5,29],[3,37],[22,34],[20,22],[9,47],[1,4],[36,46],[30,49],[1,9],[3,26],[25,41],[14,29],[1,35],[23,42],[21,32],[24,46],[3,32],[9,42],[33,37],[7,30],[29,45],[27,30],[1,7],[33,42],[17,47],[12,47],[19,41],[3,42],[24,26],[20,29],[11,23],[22,40],[9,37],[31,32],[23,46],[11,38],[27,29],[17,37],[23,30],[14,42],[28,30],[29,31],[1,8],[1,36],[42,50],[21,41],[11,18],[39,41],[32,34],[6,37],[30,38],[21,46],[16,37],[22,24],[17,32],[23,29],[3,30],[8,30],[41,48],[1,39],[8,47],[30,44],[9,46],[22,45],[7,26],[35,42],[1,27],[17,30],[20,46],[18,29],[3,29],[4,30],[3,46]], True),`
