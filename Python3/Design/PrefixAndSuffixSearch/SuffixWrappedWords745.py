from typing import List
import collections


def Trie(): return collections.defaultdict(Trie)


# Just a random key to store weight in a trie node
WEIGHT = False


class WordFilter(object):
    """
    Consider the word 'apple'. For each suffix of the word, we could insert that suffix, followed by '#', followed by the word, all into the trie.

    For example, we will insert '#apple', 'e#apple', 'le#apple', 'ple#apple', 'pple#apple', 'apple#apple' into the trie. Then for a query like prefix = "ap", suffix = "le", we can find it by querying our trie for le#ap.
    """

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix: str, suffix: str):
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]

# Runtime: 896 ms, faster than 42.19% of Python3 online submissions for Prefix and Suffix Search.
# Memory Usage: 60.8 MB, less than 24.17% of Python3 online submissions for Prefix and Suffix Search.


# import collections
# def Trie(): return collections.defaultdict(Trie)
# class WordFilter:
#     def __init__(self, words: List[str]):
#         self.trie = Trie()
#         for weight, word in enumerate(words):
#             for i in range(len(word) + 1):
#                 node = self.trie
#                 node['weight'] = weight
#                 word_to_insert = word[i:] + '#' + word
#                 for c in word_to_insert:
#                     node = node[c]
#                     node['weight'] = weight
#     def f(self, prefix: str, suffix: str):
#         node = self.trie
#         for c in suffix + '#' + prefix:
#             if c not in node:
#                 return -1
#             node = node[c]
#         return node['weight']

# Runtime: 832 ms, faster than 54.14% of Python3 online submissions for Prefix and Suffix Search.
# Memory Usage: 61 MB, less than 16.25% of Python3 online submissions for Prefix and Suffix Search.
