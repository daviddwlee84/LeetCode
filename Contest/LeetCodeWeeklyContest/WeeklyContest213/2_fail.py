class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        def start_with(cid: int, left: int):
            if left == 0:
                return 1

            return sum(start_with(i, left - 1) for i in range(cid, len(vowels)))

        return start_with(0, n)
