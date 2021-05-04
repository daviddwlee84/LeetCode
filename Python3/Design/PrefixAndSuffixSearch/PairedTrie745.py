from typing import List
import collections


def Trie(): return collections.defaultdict(Trie)


# Just a random key to store weight in a trie node
WEIGHT = False


class WordFilter(object):
    """
    Say we are inserting the word apple. We could insert ('a', 'e'), ('p', 'l'), ('p', 'p'), ('l', 'p'), ('e', 'a') into our trie. Then, if we had equal length queries like prefix = "ap", suffix = "le", we could find the node trie['a', 'e']['p', 'l'] in our trie. This seems promising.

    What about queries that aren't equal? We should just insert them like normal. For example, to capture a case like prefix = "app", suffix = "e", we could create nodes trie['a', 'e']['p', None]['p', None].
    """

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            cur = self.trie
            cur[WEIGHT] = weight
            for i, x in enumerate(word):
                # Put all prefixes and suffixes
                tmp = cur
                for letter in word[i:]:
                    tmp = tmp[letter, None]
                    tmp[WEIGHT] = weight

                tmp = cur
                for letter in word[:-i or None][::-1]:
                    tmp = tmp[None, letter]
                    tmp[WEIGHT] = weight

                # Advance letters
                cur = cur[x, word[~i]]
                cur[WEIGHT] = weight

    def f(self, prefix: str, suffix: str):
        cur = self.trie
        max_length = max(len(prefix), len(suffix))
        for a, b in zip(list(prefix) + [None] * (max_length - len(prefix)), list(suffix[::-1]) + [None] * (max_length - len(suffix))):
            if (a, b) not in cur:
                return -1
            cur = cur[a, b]
        return cur[WEIGHT]

# Runtime: 1044 ms, faster than 27.40% of Python3 online submissions for Prefix and Suffix Search.
# Memory Usage: 69.4 MB, less than 12.12% of Python3 online submissions for Prefix and Suffix Search.
