class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if ord('A') <= ord(word[0]) <= ord('Z'):
            first_capital = True
        else:
            first_capital = False

        capital = None

        for char in word[1:]:
            if capital is None:
                if ord('A') <= ord(char) <= ord('Z'):
                    if not first_capital:
                        return False
                    capital = True
                else:
                    capital = False
            else:
                if (ord('A') <= ord(char) <= ord('Z')) ^ capital:
                    return False
        return True
