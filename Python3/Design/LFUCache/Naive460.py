class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {} # key: [value, frequency, time]
        self.capacity = capacity
        self.time = 0

    def __findMinFreqOrLRU(self, my_dict):
        # Return key with minimum frequency
        minKey = min(my_dict.keys(), key=(lambda k: my_dict[k][1]))
        # If there're multiple same frequencies => use FIFO
        allMinKey = []
        for key, value in my_dict.items():
            if value[1] == my_dict[minKey][1]:
                allMinKey.append((key, value[2]))
            
        minAndLRU = min(allMinKey, key=lambda k: k[1])
            
        return minAndLRU[0]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.time += 1
        if key in self.cache:
            self.cache[key][1] += 1
            self.cache[key][2] = self.time
            return self.cache[key][0]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.time += 1
        if key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1
            self.cache[key][2] = self.time
        elif self.capacity != 0:
            if len(self.cache) == self.capacity:
                minFreqKey = self.__findMinFreqOrLRU(self.cache)
                self.cache.pop(minFreqKey)
            self.cache[key] = [value, 1, self.time]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    cache = LFUCache(2)
    cache.put(2, 1)
    cache.put(3, 2)
    print(cache.get(3))
    print(cache.get(2))
    cache.put(4, 3)
    print(cache.get(2))
    print(cache.get(3))
    print(cache.get(4))
    

if __name__ == '__main__':
    main()