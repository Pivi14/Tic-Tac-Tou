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
    if board_sum == 1:
        row = 1
        col = 1
        if board[row][col] != 0:
            row = 0
            col = 0
        ai_coord = [row, col]
        return ai_coord
    else:
        coord = ai_think(board)
        for i in range(3):
            if board[coord[i][0]][coord[i][1]] == 0:
                return coord[i]


def ai_think(new_board):
    row1 = ['row1', new_board[0][0], new_board[0][1], new_board[0][2]]
    row2 = ['row2', new_board[1][0], new_board[1][1], new_board[1][2]]
    row3 = ['row3', new_board[2][0], new_board[2][1], new_board[2][2]]
    col1 = ['col1', new_board[0][0], new_board[1][0], new_board[2][0]]
    col2 = ['col2', new_board[0][1], new_board[1][1], new_board[2][1]]
    col3 = ['col3', new_board[0][2], new_board[1][2], new_board[2][2]]
    cross1 = ['cross1', new_board[0][0], new_board[1][1], new_board[2][2]]
    cross2 = ['cross2', new_board[2][0], new_board[1][1], new_board[0][2]]
    raw_win = [row1, row2, row3, col1, col2, col3, cross1, cross2]
    one = []
    two = []
    three = []
    four = []
    five = []
    win = [[[0, 0], [0, 1], [0, 2]],
           [[1, 0], [1, 1], [1, 2]],
           [[2, 0], [2, 1], [2, 2]],
           [[0, 0], [1, 0], [2, 0]],
           [[0, 1], [1, 1], [2, 1]],
           [[0, 2], [1, 2], [2, 2]],
           [[0, 0], [1, 1], [2, 2]],
           [[2, 0], [1, 1], [0, 2]]]
    for i in raw_win:
        index = raw_win.index(i)
        if i.count(2) == 2 and i.count(0) == 1:
            five.append(win[index])
        elif i.count(1) == 2 and i.count(0) == 1:
            four.append(win[index])
        elif i.count(2) == 1 and i.count(0) == 2:
            three.append(win[index])
        elif i.count(1) == 1:
            two.append(win[index])
        elif i.count(0) == 3:
            one.append(win[index])

    if five != []:
        return five[0]
    elif four != []:
        return four[0]
    elif three != []:
        return three[0]
    elif two != []:
        return two[0]
    elif one != []:
        return one[0]





