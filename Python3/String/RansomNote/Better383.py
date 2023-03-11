class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        https://leetcode.com/problems/ransom-note/solutions/1671552/1ms-100-easy-explanation-java-solution/?orderBy=hot
        """
        if len(ransomNote) > len(magazine):
            return False

        alphabets_counter = [0] * 26
        for c in magazine:
            alphabets_counter[ord(c) - ord('a')] += 1

        for c in ransomNote:
            if alphabets_counter[ord(c) - ord('a')] == 0:
                return False
            alphabets_counter[ord(c) - ord('a')] -= 1

        return True
