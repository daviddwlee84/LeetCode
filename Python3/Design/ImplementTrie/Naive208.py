class Trie:
    """ It has the same behavior, but it is not trie """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = set()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.trie.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.trie

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for word in self.trie:
            if len(word) >= len(prefix):
                if prefix == word[:len(prefix)]:
                    return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Runtime: 1496 ms, faster than 5.02% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 20.8 MB, less than 100.00% of Python3 online submissions for Implement Trie (Prefix Tree).
