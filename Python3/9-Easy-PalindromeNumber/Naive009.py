class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        strx = str(x)

        for i in range(len(strx)//2):
            if(strx[i] != strx[len(strx)-i-1]):
                return False

        return True


def main():
    print(Solution().isPalindrome(123321))

if __name__ == '__main__':
    main()