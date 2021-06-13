from typing import List
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        total_count = Counter()
        for word in words:
            total_count += Counter(word)

        for count in total_count.values():
            if count % len(words) != 0:
                return False

        return True
