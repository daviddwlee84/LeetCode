from typing import List, Tuple


# https://leetcode.com/problems/lru-cache/solutions/45926/python-dict-double-linkedlist/
class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key: int = key  # used to remove cache
        self.value: int = value
        self.prev: Node = None
        self.next: Node = None


class DoubleLinkedList:
    def __init__(self, verbose: bool = False) -> None:
        # Dummy node that always stays at head and tail
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.verbose = verbose

    @classmethod
    def construct(cls, items: List[Tuple[int, int]]) -> 'DoubleLinkedList':
        dll = cls()
        for item in items:
            dll.append(*item)
        return dll

    @staticmethod
    def remove_node(node: Node):
        node.next.prev, node.prev.next = node.prev, node.next

    def remove_head_node(self) -> Node:
        node_to_remove = self.head.next
        if self.verbose:
            print('Removed', node_to_remove.value)
        self.remove_node(node_to_remove)
        return node_to_remove

    def add_tail_node(self, node: Node) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def append(self, key: int, value: int) -> Node:
        node = Node(key, value)
        self.add_tail_node(node)
        return node

    def print(self) -> None:
        node = self.head
        to_print = []
        while node:
            if node is not self.head and node is not self.tail:
                to_print.append((node.key, node.value))
            node = node.next
        print(to_print)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.list.remove_node(node)
        self.list.add_tail_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old one and create new one (in order to put to the last)
            self.list.remove_node(self.cache[key])
        self.cache[key] = self.list.append(key, value)

        if len(self.cache) > self.capacity:
            # Remove least recent one
            self.cache.pop(self.list.remove_head_node().key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    # Test Double Linked List
    dll = DoubleLinkedList.construct([(1, 1), (2, 2), (3, 3), (4, 4)])
    dll.print()

    obj = LRUCache(2)
    obj.put(1, 87)
    value = obj.get(1)
    print(value)
    obj.list.print()
    obj.put(2, 88)
    obj.put(3, 99)
    obj.list.print()
