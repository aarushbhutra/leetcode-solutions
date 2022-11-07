class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [x for x in board[i] if x != '.']
            col = [x for x in [board[j][i] for j in range(9)] if x != '.']
            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3) if board[x][y] != '.']
                if len(square) != len(set(square)):
                    return False
        return True

#This was too painful to make, good luck to anyone who has to read this