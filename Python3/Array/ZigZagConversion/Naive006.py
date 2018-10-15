class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        grid = [""] * numRows # Table to store temporary status of ZigZag form

        connectChar = numRows - 2 # Subtract the first and last row
        if connectChar < 0: # Prevent single row (=> modulo by 0)
            connectChar = 1
        totalChar = numRows + connectChar # Calculate how many char each pattern
        # Example:
        # numRows = 3
        # P   X  ...
        # P P X X
        # P   X
        # P is the Pattern
        for i, c in enumerate(s):
            index = i % totalChar # Position in each Pattern

            # Consider which row to put in
            if index < numRows:
                j = 2 # Initial status of j
                grid[index] += c
            else:
                grid[numRows - j] += c
                j += 1

        # Combine into one string
        result = ""
        for s in grid:
            result += s

        return result


def main():
    print(Solution().convert("PAYPALISHIRING", 3))
    print(Solution().convert("", 1))

if __name__ == '__main__':
    main()