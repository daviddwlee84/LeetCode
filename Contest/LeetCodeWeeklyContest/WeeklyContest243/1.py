class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        table = {
            chr(ord('a') + i): str(i)
            for i in range(26)
        }

        firstNum = int(''.join([table[char] for char in firstWord]))
        secondNum = int(''.join([table[char] for char in secondWord]))

        targetNum = int(''.join([table[char] for char in targetWord]))

        return firstNum + secondNum == targetNum
