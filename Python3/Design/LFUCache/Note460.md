# 460. LFU Cache

## Description

Design and implement a data structure for [Least Frequently Used (LFU) cache](https://en.wikipedia.org/wiki/Least_frequently_used). It should support the following operations: `get` and `put`.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

`put(key, value)` - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least **recently** used key would be evicted.

**Follow up**:

Could you do both operations in **O(1)** time complexity?

**Example**:

```
LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

## Solution

### Naive

* Store frequency for each key.
* The evict scenario: find the key with minimum frequency
    * If it is the only one key with minimum frequency => evict it
    * If there are multiple same frequency => use FIFO => evict the first in key

### Others

#### Ordered Dict

```python
from collections import defaultdict, OrderedDict
class LFUCache:
    def __init__(self, capacity):
        self.info = {}  # key -> [value, freq]
        self.freq = defaultdict(OrderedDict)
        self.least = 1
        self.remain = capacity

    def __touch(self, key):
        inf = self.info[key]  # [value, freq]
        self.freq[inf[1]].pop(key)
        inf[1] += 1
        if not self.freq[self.least]:
            self.least += 1
        self.freq[inf[1]][key] = inf

    def get(self, key):

        if key in self.info:
            self.__touch(key)
            return self.info[key][0]
        return -1

    def put(self, key, value):

        if key in self.info:
            self.info[key][0] = value
            self.__touch(key)
        else:
            # works for capacity = 0
            self.info[key] = [value, 1]
            self.freq[1][key] = self.info[key]
            if self.remain == 0:
                removed = self.freq[self.least].popitem(last=False)
                self.info.pop(removed[0])
                self.remain += 1
            self.remain -= 1
            self.least = 1 # put to the back
```

#### Linked List

```python
class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = dict()
        self.listmap = dict()

    def get(self, key):
        if key in self.hashmap:
            node, freq = self.hashmap.pop(key)
            self._remove_node(node, freq)
            freq += 1
            if freq not in self.listmap:
                self.listmap[freq] = LinkedList()
            self.listmap[freq]._insert(node)
            self.hashmap[key] = (node, freq)
            return node.val
        return -1

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.hashmap:
            node, freq = self.hashmap.pop(key)
            self._remove_node(node, freq)
            freq += 1
        else:
            if len(self.hashmap) == self.capacity:
                self._remove_least_freq()
            freq = 1
        if freq not in self.listmap:
            self.listmap[freq] = LinkedList()
        node = Node(key, value)
        self.listmap[freq]._insert(node)
        self.hashmap[key] = (node, freq)

    def _remove_node(self, node, freq):
        prev_node, next_node = node.prev, node.next
        if prev_node.key == -1 and next_node.key == -1:
            del self.listmap[freq]
        else:
            prev_node.next, next_node.prev = next_node, prev_node

    def _remove_least_freq(self):
        min_freq = min(self.listmap.keys())
        min_linked_list = self.listmap[min_freq]
        min_node, min_freq = self.hashmap.pop(min_linked_list.tail.prev.key)
        self._remove_node(min_node, min_freq)
```

## Reference

* [Get the maximum and minimum value in a dictionary](https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-15.php)
    * `min(d.keys(), key=lambda x: x[1])`
* [Get the key corresponding to the minimum value within a dictionary](https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary)
    * `min(d, key=d.get)`