class Node:
    def __init__(self, char, isCompleteWord = False):
        self.char = char
        self.childrenHashMap = {}
        self.isCompleteWord = isCompleteWord

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.prefixTreeRoot = Node('*')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.prefixTreeRoot
        for char in word:
            if char in node.childrenHashMap:
                node = node.childrenHashMap[char]
            else:
                new_node = Node(char) 
                node.childrenHashMap[char] = new_node
                node = new_node
        
        node.isCompleteWord = True # The last node

        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.prefixTreeRoot
        for char in word:
            if char in node.childrenHashMap:
                node = node.childrenHashMap[char]
            else:
                return False

        return node.isCompleteWord

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.prefixTreeRoot
        for char in prefix:
            if char in node.childrenHashMap:
                node = node.childrenHashMap[char]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)