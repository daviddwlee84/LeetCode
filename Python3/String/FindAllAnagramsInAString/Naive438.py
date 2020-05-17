from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_size = len(p)

        answer = []

        target = [0] * 26
        for char in p:
            target[ord(char) - ord('a')] += 1

        # only lowercase english
        currentCount = [0] * 26
        for i in range(len(s)):

            if i >= window_size:
                to_delete = s[i - window_size]
                currentCount[ord(to_delete) - ord('a')] -= 1

            to_add = s[i]
            currentCount[ord(to_add) - ord('a')] += 1

            if currentCount == target:
                answer.append(i - window_size + 1)

        return answer

# Runtime: 196 ms, faster than 28.76% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 14.7 MB, less than 8.70% of Python3 online submissions for Find All Anagrams in a String.
