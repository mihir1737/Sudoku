import sys
sys.setrecursionlimit(10**6)


def find_empty(board):
    '''Finds an empty cell and returns its position as a tuple'''
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def valid(board, pos, num):
    '''Whether a number is valid in that cell, returns a bool'''
    for i in range(9):
        if board[i][pos[1]] == num and (i, pos[1]) != pos:
            return False

    for j in range(9):
        if board[pos[0]][j] == num and (pos[0], j) != pos:
            return False

    # ex. 5-5%3 = 3 and thats where the grid starts
    g_i = pos[0] - pos[0] % 3  # row number of grid's starting cell
    g_j = pos[1] - pos[1] % 3  # col number of grid's starting cell
    for i in range(3):
        for j in range(3):
            if board[g_i + i][g_j + j] == num and (g_i + i, g_j + j) != pos:
                return False
    return True


def solve(board)-> bool: 
    '''Solves the Sudoku board via the backtracking algorithm'''
    find = find_empty(board)
    # no empty spots are left so the board is solved
    if not find:
        return True

    for nums in range(9):
        if valid(board, find, nums+1):
            board[find[0]][find[1]] = nums+1

            if solve(board):  # recursive step
                return True
            board[find[0]][find[1]] = 0
            # this number is wrong so we set it back to 0
    return False
