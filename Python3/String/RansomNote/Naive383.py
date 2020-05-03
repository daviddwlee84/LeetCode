from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_count = Counter(ransomNote)
        magazine_note_count = Counter(magazine)
    
        for char in ransom_note_count.keys():
            if char not in magazine_note_count:
                return False
                
            if magazine_note_count[char] < ransom_note_count[char]:
                # Each letter in the magazine string can only be used once in your ransom note.
                return False
        
        return True

# Runtime: 48 ms, faster than 67.14% of Python3 online submissions for Ransom Note.
# Memory Usage: 14 MB, less than 25.00% of Python3 online submissions for Ransom Note.
