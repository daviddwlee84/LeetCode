from typing import List

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_counter = defaultdict(list)
        for string in strs:
            # counter for each English letter
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            group_counter[tuple(count)].append(string)
        return group_counter.values()
