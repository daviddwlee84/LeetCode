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
