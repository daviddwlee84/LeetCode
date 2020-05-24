class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if len(searchWord) <= len(word):
                if word[:len(searchWord)] == searchWord:
                    return i + 1  # 1-indexed

        return -1
