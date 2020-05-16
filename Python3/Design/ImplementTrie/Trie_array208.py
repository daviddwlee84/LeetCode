class TrieNode:
    def __init__(self):
        # assume that all inputs are consist of lowercase letters a-z
        self.children = [None] * 26  # store TrieNode
        self.isCompleteWord = False

    def _getCharIdx(self, char: str) -> int:
        return ord(char) - ord('a')

    def containsKey(self, char: str) -> bool:
        return self.children[self._getCharIdx(char)] != None

    def get(self, char: str):
        return self.children[self._getCharIdx(char)]

    def put(self, char: str, node) -> None:
        self.children[self._getCharIdx(char)] = node

    def setEnd(self) -> None:
        self.isCompleteWord = True

    def isEnd(self) -> bool:
        return self.isCompleteWord


class Trie:
    """ It has the same behavior, but it is not trie """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if not node.containsKey(char):
                node.put(char, TrieNode())

            node = node.get(char)
        node.setEnd()

    def _searchPrefix(self, word: str) -> TrieNode:
        node = self.root
        for char in word:
            if node.containsKey(char):
                node = node.get(char)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._searchPrefix(word)
        return node != None and node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self._searchPrefix(prefix)
        return node != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Runtime: 352 ms, faster than 13.10% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 33 MB, less than 7.41% of Python3 online submissions for Implement Trie (Prefix Tree).
