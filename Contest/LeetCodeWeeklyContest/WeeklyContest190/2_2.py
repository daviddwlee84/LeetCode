class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """ two pointer """
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        left, right = 0, 0
        curr_max = 0
        total_max = 0

        while right < len(s):
            if s[right] in vowels:
                curr_max += 1
                total_max = max(total_max, curr_max)

            if right - left >= k - 1:
                # window size greater than k
                if s[left] in vowels:
                    curr_max -= 1
                left += 1

            right += 1

        return total_max
