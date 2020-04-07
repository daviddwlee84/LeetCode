from typing import List
from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = Counter(arr)
        sorted_count = sorted(list(count.items()), key=lambda x: x[0])
        
        answer = 0
        previous_i = -1
        for i, cnt in reversed(sorted_count):
            if previous_i > 0:
                if i + 1 == previous_i:
                    answer += cnt
                    
            previous_i = i
                    
        return answer            
    
