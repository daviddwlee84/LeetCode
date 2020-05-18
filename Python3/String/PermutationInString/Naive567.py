class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """ The "permutation in string" is basically the find if there is any anagram """
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        for char in s1:
            target[ord(char) - ord('a')] += 1

        current_window = [0] * 26
        for i in range(len(s2)):
            if i >= len(s1):
                # pop one char out
                current_window[ord(s2[i - len(s1)]) - ord('a')] -= 1

            current_window[ord(s2[i]) - ord('a')] += 1

            if current_window == target:
                return True

        return False
