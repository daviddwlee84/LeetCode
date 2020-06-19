class Solution:
    def longestDupSubstring(self, S: str) -> str:
        left = 0
        # maximum substring length is at most half length
        right = len(S) // 2

        answer = ''

        found = False
        while left <= right:
            length = left + (right - left) // 2

            for start in range(len(S) - length):
                candidate = S[start:start+length]
                found = self.checkAnswer(S, candidate)
                if found:
                    answer = candidate
                    left = length + 1  # try to find larger answer
                    break

            if not found:
                right = length - 1

        return answer

    def checkAnswer(self, S: str, substring: str) -> bool:
        """
        The occurrences may overlap
        '' in 'anystring' is True
        # https://stackoverflow.com/questions/10648490/removing-first-appearance-of-word-from-a-string
        """
        first_start = S.find(substring)
        return substring in S[first_start + 1:]

# TLE
