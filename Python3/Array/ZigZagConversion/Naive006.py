class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        grid = [""] * numRows

        connectChar = numRows - 2
        if connectChar < 0:
            connectChar = 1
        totalChar = numRows + connectChar
        for i, c in enumerate(s):
            index = i % totalChar
            if index < numRows:
                j = 2
                grid[index] += c
            else:
                grid[numRows - j] += c
                j += 1
        result = ""
        for s in grid:
            result += s

        return result


def main():
    print(Solution().convert("PAYPALISHIRING", 3))
    print(Solution().convert("", 1))

if __name__ == '__main__':
    main()