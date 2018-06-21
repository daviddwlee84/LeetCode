class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        """
        00 ┃ 01 ┃ 02
        ━━━╋━━━━╋━━━
        10 ┃ 11 ┃ 12
        ━━━╋━━━━╋━━━
        20 ┃ 21 ┃ 22
        """
        GridTable = {}
        
        VerticalLineTable = {}
        HorizontalLineTable = {}
        
        GridInitialKey = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
        for i in range(9):
            GridTable[GridInitialKey[i]] = set()
            VerticalLineTable[i] = set()
            HorizontalLineTable[i] = set()

        for row in range(9):
            for col in range(9):
                current = board[row][col]
                if current == '.':
                    continue

                if current in VerticalLineTable[col]:
                    return False
                else:
                    VerticalLineTable[col].add(current)
                
                if current in HorizontalLineTable[row]:
                    return False
                else:
                    HorizontalLineTable[row].add(current)
                
                if current in GridTable[str(row//3)+str(col//3)]:
                    return False
                else:
                    GridTable[str(row//3)+str(col//3)].add(current)

        return True
                