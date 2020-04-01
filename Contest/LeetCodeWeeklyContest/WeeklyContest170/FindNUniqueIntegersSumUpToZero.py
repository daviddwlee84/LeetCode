class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabetDict = {i + 1: chr(i + 97) for i in range(26)}
        i = 0
        nums = []
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                nums.append(int(s[i:i+2]))
                i = i + 3
            else:
                nums.append(int(s[i]))
                i = i + 1
        ans = ''
        for num in nums:
            ans += alphabetDict[num]

        return ans
