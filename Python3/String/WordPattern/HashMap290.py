class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match = {}
        inverse_match = {}
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        for c, word in zip(pattern, words):
            if c not in match:
                match[c] = word
                if word in inverse_match:
                    return False
                inverse_match[word] = c
            else:
                if match[c] != word:
                    return False

        return True
