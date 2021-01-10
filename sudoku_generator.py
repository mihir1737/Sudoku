from sudoku_algorithm import valid, solve
import random


def generate(level):
    '''
    Randomly generates a Sudoku grid/board
    level: 1, 2 or 3
    complexity of game increasing with level.
    '''
    if level not in range(1, 4):
        #print(level)
        raise ValueError("Level must be in 1 to 3.")
    board = [[0 for _ in range(9)] for _ in range(9)]
    # puts one random number, then solves the board to generate a board
    for i in range(9):
        for j in range(9):
            if random.randint(1, 10) >= 6:
                # plug in random number at i,j spot.
                board[i][j] = random.randint(1, 9)
                if not valid(board, (i, j), board[i][j]):
                    board[i][j] = 0
    if not solve(board):
        return generate(level)
    count = 45 - level * 7
    total = 81
    while total > count:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if board[x][y] != 0:
            board[x][y] = 0
            total -= 1
    return board
