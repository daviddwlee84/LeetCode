import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data:
            return False
        else:
            self.data.add(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            self.data.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        n = len(self.data)
        items = list(self.data)
        index = random.randint(0, n - 1)
        return items[index]

        # Runtime: 448 ms, faster than 12.34% of Python3 online submissions for Insert Delete GetRandom O(1).
        # Memory Usage: 18 MB, less than 22.50% of Python3 online submissions for Insert Delete GetRandom O(1).

        # Other solutions
        # return random.choice(list(self.data))
        # Runtime: 424 ms, faster than 20.14% of Python3 online submissions for Insert Delete GetRandom O(1).
        # Memory Usage: 18.2 MB, less than 12.55% of Python3 online submissions for Insert Delete GetRandom O(1).


        # index = int(random.random() * len(self.data))
        # Runtime: 412 ms, faster than 22.27% of Python3 online submissions for Insert Delete GetRandom O(1).
        # Memory Usage: 18.2 MB, less than 10.63% of Python3 online submissions for Insert Delete GetRandom O(1).
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()