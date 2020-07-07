class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.set.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.

        backtracking to search all the .
        """

        if '.' in word:
            index = word.find('.')
            found = False
            for i in range(ord('a'), ord('z') + 1):
                found |= self.search(word[:index] + chr(i) + word[index + 1:])
            return found
        else:
            return word in self.set


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# TLE