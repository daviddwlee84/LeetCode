from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if self.earlyStop(moves):
            return "Pending"

        table = [['N' for _ in range(3)] for _ in range(3)] 
        # build table
        for i, (x, y) in enumerate(moves):
            if i % 2 == 0: # player A
                table[x][y] = 'A' # X
            else: # player B
                table[x][y] = 'B' # B
                
        winner = self.checkWin(table)
        if winner == 'No':
            if len(moves) == 9:
                return "Draw"
            else:
                return "Pending"
        else:
            return winner
                
    def earlyStop(self, moves):
        if len(moves) < 5:
            return True
        return False

    def checkWin(self, table):
        # same row
        for row in range(3):
            if table[0][row] == table[1][row] == table[2][row] and table[0][row] != 'N':
                return table[0][row]
            
        # col
        for col in range(3):
            if table[col][0] == table[col][1] == table[col][2] and table[col][0] != 'N':
                return table[col][0]    
            
        # cross
        if table[0][0] == table[1][1] == table[2][2] and table[1][1] != 'N':
            return table[1][1]
        if table[2][0] == table[1][1] == table[0][2] and table[1][1] != 'N':
            return table[1][1]
 
        return 'No'
 
if __name__ == "__main__":
    moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    print(Solution().tictactoe(moves)) # A

    moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    print(Solution().tictactoe(moves)) # B

    moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    print(Solution().tictactoe(moves)) # Draw

    moves = [[0,0],[1,1]]
    print(Solution().tictactoe(moves)) # Pending
