from typing import List

# TODO: maybe try linear hashing?!

class MyHashSet:
    """
    https://leetcode.com/problems/design-hashset/discuss/210494/Real-Python-Solution-no-cheating-open-addressing
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        INIT_CAPACITY = 8
        LOAD_FACTOR = 2 / 3
        self.capacity = INIT_CAPACITY
        self.size = 0
        self.slots = [None] * INIT_CAPACITY
        self.load_factor = LOAD_FACTOR

    def _hash_func(self, key: int) -> int:
        """
        can be modified to hash other hashable objects
        like built-in python hash function
        """
        return key % self.capacity

    def _double_hashing(self, key: int, slots: List[int] = None) -> int:
        """
        If we add an element that is hashed to the same index as another key,
        then we apply a secondary operation on the index until we find an empty spot
        (or a previously removed spot). This is called double hashing.
        """
        if not slots:
            slots = self.slots

        hash_idx = self._hash_func(key)
        while slots[hash_idx] is not None:
            hash_idx = self._hash_func(5 * hash_idx + 1)

        return hash_idx

    # All hash must also change to linear
    #
    # def _linear_hashing(self, key: int, slots: List[int] = None) -> int:
    #     """
    #     Linearly find the next empty slot. (unused here)
    #     """
    #     if not slots:
    #         slots = self.slots

    #     hash_idx = self._hash_func(key)
    #     while slots[hash_idx] is not None:
    #         hash_idx += 1
    #         hash_idx %= len(slots)

    #     return hash_idx

    def add(self, key: int) -> None:
        # Expands the capacity with twice of it size when the load factor exceed LOAD_FACTOR
        if self.size / self.capacity >= self.load_factor:
            self.capacity *= 2  # same as <<= 1
            new_slots = [None] * self.capacity
            # Copy the old slots and re-hash (remove TOMBSTONEs)
            for i in range(self.capacity // 2):
                if self.slots[i] and self.slots[i] != '==TOMBSTONE==':
                    hash_idx = self._double_hashing(self.slots[i], new_slots)
                    new_slots[hash_idx] = self.slots[i]
            self.slots = new_slots

        hash_idx = self._find_key(key, find_empty=True)
        if self.slots[hash_idx] != key:
            self.size += 1
            self.slots[hash_idx] = key

    def remove(self, key: int) -> None:
        hash_idx = self._find_key(key, find_empty=False)
        if hash_idx >= 0:
            self.slots[hash_idx] = '==TOMBSTONE=='
            self.size -= 1

    def _find_key(self, key: int, find_empty: bool) -> int:
        """
        Check if a key is in the HashSet
        if find_empty, then it will find an empty slot
        """
        hash_idx = self._hash_func(key)

        while self.slots[hash_idx] is not None:
            if self.slots[hash_idx] == key:
                return hash_idx

            if find_empty and self.slots[hash_idx] == '==TOMBSTONE==':
                return hash_idx

            hash_idx = self._hash_func(5 * hash_idx + 1)

        if find_empty:
            return hash_idx

        return -1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self._find_key(key, find_empty=False) >= 0

# Double Hashing
# Runtime: 252 ms, faster than 55.12% of Python3 online submissions for Design HashSet.
# Memory Usage: 18.2 MB, less than 58.93% of Python3 online submissions for Design HashSet.

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
