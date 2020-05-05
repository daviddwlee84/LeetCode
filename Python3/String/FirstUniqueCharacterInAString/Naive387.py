from collections import OrderedDict
# https://docs.python.org/3.8/library/collections.html#ordereddict-objects
# https://stackoverflow.com/questions/21062781/shortest-way-to-get-first-item-of-ordereddict-in-python-3

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_appear = set()
        unique_index = OrderedDict()
        for i, char in enumerate(s):
            if char not in char_appear:
                char_appear.add(char)
                unique_index[char] = i
            else:
                if char in unique_index:
                    unique_index.pop(char)
    
        if not unique_index:
            return -1
        else:
            # if use normal dict, we should iterate through all items and return the minimum index
            return unique_index.popitem(last=False)[1]

# Runtime: 96 ms, faster than 78.76% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 13.8 MB, less than 6.52% of Python3 online submissions for First Unique Character in a String.
