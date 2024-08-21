# 注意for 和 return 的缩进关系，别循环一次就return了

from types import list

# N皇后
class Solution:
    def solve_Queens(self, n: int) -> list[list[str]]:
        self.result = []

        chess_board = ['.' * n for _ in range(n)]
        self.backtracking(n ,0 ,chess_board)
        return[[''.join(row) for row in item] for item in self.result]
    
    def backtracking(self, n: int, row: int, chess_board:list[str]):
        if row == n:
            self.result.append(chess_board[:])
            return
        
        for col in range(n):
            if self.is_valid(row, col, chess_board):
                chess_board[row] = chess_board[row][:col] + 'Q' + chess_board[row][col+1:] 
                self.backtracking(n, row + 1, chess_board)
                chess_board[row] = chess_board[row][:col] + '.' + chess_board[row][col+1:]
        return  # 注意return在for之外，且可以省略

    def is_valid(self, row: int, col: int, chess_board: list[str]) -> bool:
        # 检查列，当前列存在Q则不合法
        for i in range(row):
            if chess_board[i][col] == 'Q':
                return False
        
        # 往下搜索，只用检查当前左上和右上就够了，不用管左下和右下
        # 检查45°角是否有皇后
        i, j = row - 1, col - 1
        while i >= 0 and j>= 0:
            if chess_board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # 135°
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chess_board):  # 注意边界条件
            if chess_board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    

# 解数独，二维递归
class SudokuSolution:
    def solve_sudoku():
        return
    def backtracking():
        return
    def is_valid():
        # 同一行是否冲突
        # 同一列是否冲突
        # 同一九宫格是否冲突
        return
            
    
    