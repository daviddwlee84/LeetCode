from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = deque()  # manage key, which stay which leave
        self.map = {}  # manage value, store and access value in O(1)

    def get(self, key: int) -> int:
        if key in self.map:
            # https://realpython.com/linked-lists-python/#introducing-collectionsdeque
            # update the recent used
            self.cache.remove(key)
            self.cache.appendleft(key)
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # already in cache, just update key
            self.cache.remove(key)
            self.cache.appendleft(key)
            # value might be different
            self.map[key] = value
        else:
            if len(self.cache) == self.capacity:
                # get rid of the least recent used
                old_key = self.cache.pop()
                self.map.pop(old_key)

            self.cache.appendleft(key)
            self.map[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
