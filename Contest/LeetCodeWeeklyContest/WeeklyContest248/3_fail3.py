class Solution:
    memory = {1: 5}
    MOD = 10 ** 9 + 7

    def countGoodNumbers(self, n: int) -> int:
        """
        even = 0, 2, 4, 6, 8
        prime = 2, 3, 5, 7
        """

        if n not in self.memory:
            if n % 2 == 0:
                self.memory[n] = self.countGoodNumbers(n - 1) * 4 % self.MOD
            else:
                self.memory[n] = self.countGoodNumbers(n - 1) * 5 % self.MOD

        return self.memory[n]

# Recursion Error: maximum recursion depth exceeded in comparison
