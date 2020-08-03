class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = 0
        for char in word:
            caps += int(char.isupper())
        
        return (word[0].isupper() and caps == 1) or len(word) == caps or caps == 0
