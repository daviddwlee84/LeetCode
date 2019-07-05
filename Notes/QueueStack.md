# Queue & Stack

* restrict the processing order

Goals:

* Understand the principle of the processing orders of FIFO and LIFO;
* Implement these two data structures;
* Be familiar with the built-in queue and stack structure;
* Solve basic queue-related problems, especially BFS;
* Solve basic stack-related problems problems;
* Understand how system stack helps you when you solve problems using DFS and other recursion algorithms;

## Queue: First-in-first-out Data Structure

Goals:

* Understand the definition of FIFO and queue;
* Be able to implement a queue by yourself;
* Be familiar with the built-in queue structure;
* Use queue to solve simple problems.

### First-in-first-out Data Structure

### Queue - Implementation

should support two operations: `enqueue` and `dequeue`

```cpp
#include <vector>

using namespace std;

class MyQueue {
    private:
        // store elements
        vector<int> data;
        // a pointer to indicate the start position
        int p_start;
    public:
        MyQueue() {p_start = 0;}
        /** Insert an element into the queue. Return true if the operation is successful. */
        bool enQueue(int x) {
            data.push_back(x);
            return true;
        }
        /** Delete an element from the queue. Return true if the operation is successful. */
        bool deQueue() {
            if (isEmpty()) {
                return false;
            }
            p_start++;
            return true;
        };
        /** Get the front item from the queue. */
        int Front() {
            return data[p_start];
        };
        /** Checks whether the queue is empty or not. */
        bool isEmpty()  {
            return p_start >= data.size();
        }
};
```

## Circular Queue

> Links searched when designing circular queue
>
> * [CppTest](https://cpptest.sourceforge.io/tutorial.html)
> * [cppreference.com - std::vector](https://en.cppreference.com/w/cpp/container/vector)
> * [How to set initial size of std::vector?](https://stackoverflow.com/questions/11457571/how-to-set-initial-size-of-stdvector)

## Queue & BFS

One common application of Breadth-first Search (BFS) is to find the shortest path from the root node to the target node.

using BFS:

* do traversal
* find the shortest path

Typically, it happens in a tree or a graph, or more abstract scenarios.

* nodes: actual node or status
* edges: actual edge or transition

### Template I

```java
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    // BFS
    while (queue is not empty) {
        step = step + 1;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                add next to queue;
            }
            remove the first node from queue;
        }
    }
    return -1;          // there is no path from root to target
}
```

### Template II - never visit a node twice

e.g. in graph with cycle => cause infinite loop

Add a "hast set" to solve this problem. (`Set<Node> visited;`)

```java
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    Set<Node> visited;  // store all the nodes that we've visited
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    add root to visited;
    // BFS
    while (queue is not empty) {
        step = step + 1;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                if (next is not in used) {
                    add next to queue;
                    add next to visited;
                }
                remove the first node from queue;
            }
        }
    }
    return -1;          // there is no path from root to target
}
```

> There are some cases where one does not need keep the visited hash set:
>
> * You are absolutely sure there is no cycle, for example, in tree traversal;
> * You do want to add the node to the queue multiple times.
