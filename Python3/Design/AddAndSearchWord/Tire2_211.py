class WordDictionary:
    """
    Self as a Trie node
    https://leetcode.com/problems/design-add-and-search-words-data-structure/solutions/3313792/image-explanation-easy-trie-c-java-python/
    """

    def __init__(self):
        self.children = {}
        self.is_word = False

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self
        for i, char in enumerate(word):
            if char == '.':
                for child in node.children.values():
                    if child.search(word[i + 1:]):
                        return True
                return False

            if char not in node.children:
                return False
            node = node.children[char]

        return node is not None and node.is_word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
