class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        vowel_count = [0]
        max_num = 0
        for char in s:
            if char in vowels:
                vowel_count.append(vowel_count[-1] + 1)
            else:
                vowel_count.append(vowel_count[-1])

        for i in range(len(s) - k + 1):
            max_num = max(max_num, vowel_count[i + k] - vowel_count[i])

        return max_num
