"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        Value = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        MinusValue = {4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}


def main():
    Solution().intToRoman(10)

if __name__ == "__main__":
    main()
