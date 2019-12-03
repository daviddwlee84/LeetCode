from typing import List

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            ans[tuple(sorted(string))].append(string)
        return ans.values()
