class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        put_one = True
        answer = []
        while i < len(word1) or j < len(word2):
            if put_one and i < len(word1):
                answer.append(word1[i])
                i += 1
            elif not put_one and j < len(word2):
                answer.append(word2[j])
                j += 1
            put_one = not put_one

        return ''.join(answer)
