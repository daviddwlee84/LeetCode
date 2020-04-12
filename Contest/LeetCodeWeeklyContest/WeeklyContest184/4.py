"""
https://www.geeksforgeeks.org/ways-color-3n-board-using-4-colors/
https://www.geeksforgeeks.org/ways-to-paint-n-paintings-such-that-adjacent-paintings-dont-have-same-colors/

If fill row depend on previous row

A B C (ori is 3 color)

* 2 color => 2
  * B A B
  * B C B
* 3 color => 2
  * B C A
  * C A B

A B A (ori is 2 color)

* 2 color => 3
  * B A B
  * B C B
  * C A C
* 3 color => 2
  * C A B
  * B A C

If fill single row (initial condition)

* 2 color
  * 3 * 2 * 1 = 6
    * A B A
    * B A B
    * A C A
    * C A C
    * B C B
    * C B C
* 3 color (rest)
  * 3 * 2 * 1 = 6
    * A B C
    * B C A
    * C A B
    * B A C
    * A C B
    * C B A
"""

TO_MOD = 1e9 + 7


class Solution:
    def numOfWays(self, n: int) -> int:
        temp = 0
        # Initial: fill single row
        color2 = 6
        color3 = 6

        for _ in range(2, n + 1, 1):
            temp = color3  # because we will override color3
            color3 = (2 * color2 + 2 * color3) % TO_MOD
            color2 = (2 * temp + 3 * color2) % TO_MOD

        num = (color3 + color2) % TO_MOD

        return int(num)
