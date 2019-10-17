import random
import copy

def ai_move(board, difficult):
    main_board = board
    if difficult == 'E':
        coord = ai_easy(main_board)
        return coord
    elif difficult == 'H':
        coord = ai_impossible(main_board)
        return coord

def ai_easy(board):
    row = None
    col = None
    while row == None:
        row = random.randrange(0, 3)
        col = random.randrange(0, 3)
        if board[row][col] != 0:
            row = None
            col = None
    ai_coord = [row, col]
    return ai_coord


def ai_impossible(board):
    board_sum = 0
    for i in range(len(board)):
        for y in range(len(board[i])):
            board_sum = board_sum + board[i][y]
    if board_sum == 0:
        ai_coord = [0, 0]
        return ai_coord
    elif board_sum == 1:
        row = 1
        col = 1
        if board[row][col] != 0:
            row = 0
            col = 0
        ai_coord = [row, col]
        return ai_coord
    else:
        new_board = copy.deepcopy(board)
        for x in range(len(board)):
            for z in range(len(board[x])):
                if board[x][z] == 0:
                    board[x][z] = 3
                elif board[x][z] == 1:
                    board[x][z] = -1
                elif board[x][z] == 2:
                    board[x][z] = 1
        coord = ai_think(new_board)
        for w in range(3):
            if board[coord[w][0]][coord[w][1]] == 0:
                return coord[w]


def ai_think(new_board):
    row1 = new_board[0][0] + new_board[0][1] + new_board[0][2]
    row2 = new_board[1][0] + new_board[1][1] + new_board[1][2]
    row3 = new_board[2][0] + new_board[2][1] + new_board[2][2]
    col1 = new_board[0][0] + new_board[1][0] + new_board[2][0]
    col2 = new_board[0][1] + new_board[1][1] + new_board[2][1]
    col3 = new_board[0][2] + new_board[1][2] + new_board[2][2]
    cross1 = new_board[0][0] + new_board[1][1] + new_board[2][2]
    cross2 = new_board[2][0] + new_board[1][1] + new_board[0][2]
    raw_win = [row1, row2, row3, col1, col2, col3, cross1, cross2]
    for i in raw_win:
        if i == 2:
            raw_win[i] = 5
        elif i == -2:
            raw_win[i] = 4
        elif i == 1:
            raw_win[i] = 3
        elif i == -1:
            raw_win[i] = 2
        elif i == 0:
            raw_win[i] = 2
        elif i == 9:
            raw_win[i] = 1

    win = [[raw_win[0], [0, 0], [0, 1], [0, 2]],
           [raw_win[1], [1, 0], [1, 1], [1, 2]],
           [raw_win[2], [2, 0], [2, 1], [2, 2]],
           [raw_win[3], [0, 0], [1, 0], [2, 0]],
           [raw_win[4], [0, 1], [1, 1], [2, 1]],
           [raw_win[5], [0, 2], [1, 2], [2, 2]],
           [raw_win[6], [0, 0], [1, 1], [2, 2]],
           [raw_win[7], [2, 0], [1, 1], [0, 2]]]
    win.sort(reverse=True)
    line = win[0][1:]
    return line

