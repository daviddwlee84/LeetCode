class Solution:
    memory = {1: 5}
    MOD = 10 ** 9 + 7

    def countGoodNumbers(self, n: int) -> int:
        """
        even = 0, 2, 4, 6, 8
        prime = 2, 3, 5, 7
        """

        max_mem = max(self.memory)
        for i in range(max_mem + 1, n + 1):
            if i % 2 == 0:
                self.memory[i] = self.memory[i - 1] * 4 % self.MOD
            else:
                self.memory[i] = self.memory[i - 1] * 5 % self.MOD

        return self.memory[n]

# MLE
# 806166225460393
