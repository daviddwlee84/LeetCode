from collections import defaultdict


class TireNode:
    def __init__(self):
        self.children = defaultdict(TireNode)
        self.isWord = False


class WordDictionary:
    """
    https://leetcode.com/problems/add-and-search-word-data-structure-design/discuss/59725/Python-easy-to-follow-solution-using-Trie.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TireNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.

        backtracking to search all the .
        """
        return self.dfs(self.root, word)

    def dfs(self, node: TireNode, word: str) -> bool:
        if not word:
            return node.isWord

        if word[0] == '.':
            return any(self.dfs(next_node, word[1:]) for next_node in node.children.values())
        else:
            if word[0] in node.children:
                return self.dfs(node.children[word[0]], word[1:])
            else:
                return False

# Runtime: 508 ms, faster than 15.68% of Python3 online submissions for Add and Search Word - Data structure design.
# Memory Usage: 29.9 MB, less than 17.31% of Python3 online submissions for Add and Search Word - Data structure design.
