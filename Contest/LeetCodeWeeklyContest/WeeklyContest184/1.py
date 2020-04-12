from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = set()
        for word in words:
            for another_word in words:
                if len(word) < len(another_word):
                    if word in another_word:
                        answer.add(word)

        return list(answer)

# ["leetcoder","leetcode","od","hamlet","am"]
