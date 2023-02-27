from typing import List, Tuple


# https://leetcode.com/problems/lru-cache/solutions/45926/python-dict-double-linkedlist/
class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key: int = key  # used to remove cache
        self.value: int = value
        self.prev: Node = None
        self.next: Node = None
    
    def __repr__(self) -> str:
        return 'Node' + str((self.key, self.value))


class DoubleLinkedList:
    def __init__(self, verbose: bool = False) -> None:
        # Dummy node that always stays at head and tail
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.verbose = verbose

    @classmethod
    def construct(cls, items: List[Tuple[int, int]], verbose: bool = False) -> 'DoubleLinkedList':
        dll = cls(verbose)
        for item in items:
            dll.append(*item)
        return dll

    def remove_node(self, node: Node):
        if self.verbose:
            print('Remove', node)
        node.next.prev, node.prev.next = node.prev, node.next

    def remove_head_node(self) -> Node:
        node_to_remove = self.head.next
        self.remove_node(node_to_remove)
        return node_to_remove

    def add_tail_node(self, node: Node) -> None:
        if self.verbose:
            print('Append', node)
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

if __name__ == '__main__':
    # Test Double Linked List
    dll = DoubleLinkedList.construct([(1, 1), (2, 2), (3, 3), (4, 4)], verbose=True)
    dll.print()

    node1 = dll.append(5, 5)
    dll.print()

    node2 = Node(6, 6)
    dll.add_tail_node(node2)
    dll.print()

    dll.remove_head_node()
    dll.print()

    dll.remove_node(node1)
    dll.print()
