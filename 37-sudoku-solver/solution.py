class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append(9*i+j)
        # solve with backtracking
        idx = 0
        while idx < len(empty):
            r = empty[idx] // 9
            c = empty[idx] % 9
            # if a cell is empty, try out 1~9 and see which are valid
            # leave all possible numbers in the cell and assume the first number is correct
            if board[r][c] == '.':
                board[r][c] = '123456789.'
                for i in range(9):
                    if i != r and board[i][c] != '.':
                        board[r][c] = board[r][c].replace(board[i][c][0], '')
                for j in range(9):
                    if j != c and board[r][j] != '.':
                        board[r][c] = board[r][c].replace(board[r][j][0], '')
                for k in range(9):
                    if ((r//3)*3+k//3 != r or (c//3)*3+k%3 != c) and board[(r//3)*3+k//3][(c//3)*3+k%3] != '.':
                        board[r][c] = board[r][c].replace(board[(r//3)*3+k//3][(c//3)*3+k%3][0], '')
            # if a cell is nonempty, it must be that the first number is incorrect and caused a contradiction
            # thus, remove the first number
            else:
                board[r][c] = board[r][c][1:]
            # if the cell has no possible values after checking or modifying, go back to the previous cell
            if board[r][c] == '.':
                idx -= 1
            # otherwise, assume the first number to be correct and move on
            else:
                idx += 1
        # all the cells with the first numbers have satisfied sudoku rules
        # thus, clear the remaining part
        for i in range(9):
            for j in range(9):
                board[i][j] = board[i][j][0]
