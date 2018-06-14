class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            # Negative number isn't palindrome
            return False
        elif x == 0:
            # Zero is palindrome
            return True
        else:
            # Reverse x
            reverse_x = 0
            temp = x
            while temp != 0:
                # reverse_x shift left 1 space and add LSB of temp
                # (So the LSB of temp will be the MSB of reverse_x and so on.)
                reverse_x = reverse_x*10 + temp%10
                temp //= 10
            
            # Compare x with reverse x
            if x == reverse_x:
                return True
            else:
                return False


def main():
    print(Solution().isPalindrome(123321))
    print(Solution().isPalindrome(123421))

if __name__ == '__main__':
    main()