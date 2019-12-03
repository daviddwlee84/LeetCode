from typing import List

from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_counter = {}
        output = []
        for string in strs:
            added = False
            curr_counter = Counter(string)
            for idx, (head_counter, length) in group_counter.items():
                if length != len(string):
                    continue
                if head_counter == curr_counter:
                    output[idx].append(string)
                    added = True
                    break
            if not added:
                group_counter[len(output)] = (curr_counter, len(string))
                output.append([string])
        
        return output

# Time Limit Exceeded
