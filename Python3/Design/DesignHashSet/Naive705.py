class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = 0

    def add(self, key: int) -> None:
        self.data |= (2 << key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.data ^= (2 << key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return bool(self.data & (2 << key))

# Runtime: 248 ms, faster than 56.69% of Python3 online submissions for Design HashSet.
# Memory Usage: 17.7 MB, less than 92.86% of Python3 online submissions for Design HashSet.

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
