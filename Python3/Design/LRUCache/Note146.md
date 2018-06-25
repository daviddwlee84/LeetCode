# 146. LRU Cache

## Description

Design and implement a data structure for [Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU). It should support the following operations: `get` and `put`.

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

`put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

**Follow up**:

Could you do both operations in **O(1)** time complexity?

**Example**:

```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

## Solution

### Naive

* Use a list to store key which is used to check if key is in cache.
* Use a dict to store key-value pair.

### Ordered Dict

[Python collections - Container datatypes: OrderedDict objects](https://docs.python.org/3.6/library/collections.html#ordereddict-objects)

### Others solution

#### Double Linked list

```python
class ListNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next, self.prev = None, None
    def printList(self):
        now = self
        while now:
            if now == self: print('head->', end='')
            if now.val: print('({},{})->'.format(now.key, now.val), end='')
            now = now.next
        print()

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.start, self.end = ListNode(), ListNode()
        self.hashTable = {}
        self.start.next = self.end
        self.end.prev = self.start

    # utils function
    def removeNode(self, key):
        node = self.hashTable[key]
        L, R = node.prev, node.next
        L.next, R.prev = node.next, node.prev

    def insertNodeEnd(self, key):
        node = self.hashTable[key]
        L, R = self.end.prev, self.end
        L.next, node.prev = node, L
        R.prev, node.next = node, R

    def insertHash(self, key, value):
        self.hashTable[key] = ListNode(key, value)

    def removeHash(self, key):
        del self.hashTable[key]

    def get(self, key):
        if not (key in self.hashTable): return -1
        self.removeNode(key)
        self.insertNodeEnd(key)
        return self.hashTable[key].val

    def put(self, key, value):
        if key in self.hashTable:
            self.hashTable[key].val = value
            self.removeNode(key)
        else:
            self.insertHash(key, value)
        self.insertNodeEnd(key)  
        keyToBeRemoved = self.start.next.key
        if len(self.hashTable) > self.size:
            self.removeNode(keyToBeRemoved)
            self.removeHash(keyToBeRemoved)
```