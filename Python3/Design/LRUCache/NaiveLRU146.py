class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keys = [] # Store key in order. Bottom is LRU.
        self.valuePair = {} # Store key-value pair. (Hash map)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keys:
            # Refresh the key to the LRU
            self.keys.remove(key)
            self.keys.insert(0, key)

            return self.valuePair[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.keys:
            # Update key value
            # Refresh the key to the LRU
            self.keys.remove(key)
            self.keys.insert(0, key)
            self.valuePair[key] = value
        else:
            # Insert new key
            self.keys.insert(0, key)
            self.valuePair[key] = value
            if len(self.keys) > self.capacity:
                remove = self.keys.pop()
                self.valuePair.pop(remove)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))       # returns 1
    cache.put(3, 3)           # evicts key 2
    print(cache.get(2))       # returns -1 (not found)
    cache.put(4, 4)           # evicts key 1
    print(cache.get(1))       # returns -1 (not found)
    print(cache.get(3))       # returns 3
    print(cache.get(4))       # returns 4

if __name__ == '__main__':
    main()