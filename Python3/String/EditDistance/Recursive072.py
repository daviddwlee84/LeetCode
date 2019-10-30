class Solution:
    def minDistance(self, word1, word2):
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        # the same, do nothing
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        # insert word1[0] to the front of word2
        insert = 1 + self.minDistance(word1, word2[1:])
        # delete word1[0]
        delete = 1 + self.minDistance(word1[1:], word2)
        # replace word1[0] as word2[0]
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)