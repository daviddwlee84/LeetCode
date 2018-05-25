class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            A = 0
            B = x
            while B != 0:
                A = A*10 + B%10
                B //= 10
            if x == A:
                return True
            else:
                return False


def main():
    print(Solution().isPalindrome(123321))
    print(Solution().isPalindrome(123421))

if __name__ == '__main__':
    main()