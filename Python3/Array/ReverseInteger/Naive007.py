class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = -x
            outputlst = '-'
        else:
            outputlst = ''
        
        temp = str(x)
        for i in range(len(temp), 0, -1):
            outputlst += temp[i-1]

        result = int(outputlst)
        if abs(result) < 2**31:
            return result
        else:
            return 0


def main():
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))

if __name__ == '__main__':
    main()