from typing import List

# TODO

# [Verbal arithmetic - Wikipedia](https://en.wikipedia.org/wiki/Verbal_arithmetic#Solving_cryptarithms)
# [Solving Cryptarithmetic Puzzles | Backtracking-8 - GeeksforGeeks](https://www.geeksforgeeks.org/solving-cryptarithmetic-puzzles-backtracking-8/)
# [Solving Alphametics with Python | Enigmatic Code](https://enigmaticcode.wordpress.com/2016/06/22/solving-alphametics-with-python/)
# [Simple cryptarithmetic puzzle solver in Java, C, and Python](https://gist.github.com/vo/2481737)


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        chars = set()
        for word in [*words, result]:
            for char in word:
                chars.add(char)

        if len(chars) > 10:
            return False
