from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = OrderedDict()    
        self.remain = capacity # Empty space remain in cache
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        value = self.dic.pop(key)
        self.dic[key] = value
        return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False) # pop with FIFO order
        self.dic[key] = value