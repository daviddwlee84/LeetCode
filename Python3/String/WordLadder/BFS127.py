from typing import List
from collections import defaultdict, deque


class Solution:
    def _preprocess(self, wordList: List[str]):
        """ get a hashmap for all generic states/words """

        # {intermediate_state: [all possible word]}
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(self.L):
                # replace each char position with *
                intermediate_state = word[:i] + "*" + word[i+1:]
                all_combo_dict[intermediate_state].append(word)
        return all_combo_dict

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        self.L = len(beginWord)  # all words are same length

        all_combo_dict = self._preprocess(wordList)

        # Queue for BFS
        queue = deque([(beginWord, 1)])  # (word, depth)
        # Visited to make sure we don't repeat processing same word
        visited = {beginWord: True}

        while queue:
            current_word, depth = queue.pop()
            for i in range(self.L):
                intermediate_state = current_word[:i] + \
                    "*" + current_word[i+1:]

                for word in all_combo_dict[intermediate_state]:
                    # attempt to visit words match intermediate_state

                    if word == endWord:
                        # found word
                        return depth + 1

                    if word not in visited:
                        # first time visit
                        visited[word] = True
                        queue.appendleft((word, depth + 1))

                # clean up since we have attempt visit all words in it
                all_combo_dict[intermediate_state] = []

        return 0

# Runtime: 124 ms, faster than 82.26% of Python3 online submissions for Word Ladder.
# Memory Usage: 16.4 MB, less than 31.03% of Python3 online submissions for Word Ladder.
