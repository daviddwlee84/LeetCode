class Solution:
    def isHappy(self, n: int) -> bool:
        square = {
            0: 0,
            1: 1,
            2: 4,
            3: 9,
            4: 16,
            5: 25,
            6: 36,
            7: 49,
            8: 64,
            9: 81,
        }

        appeared = set()
        while n != 1:
            temp = 0
            while n > 0:
                temp += square[n % 10]
                n //= 10
            n = temp
            if n not in appeared:
                appeared.add(n)
            else:
                # loop
                return False
        return True
