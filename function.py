import copy

def init_board():
    matrix = []
    for i in range(3):
        row = []
        matrix.append(row)
        for y in range(3):
            row.append(0)
    return matrix

def get_move(old_board):
    board = old_board
    row_list = ['A', 'B', 'C']
    col_list = [1, 2, 3]
    row = None
    col = None
    c = 0
    while c == 0:
        while not row in row_list:
            try:
                row = input("Give me the row's letter A, B or C: ").upper()
            except:
                print("Please enter a valid letter!")
                continue
        while not col in col_list:
            try:
                col = int(input("Give me the column's number 1, 2, or 3: "))
            except:
                print("Please enter a valid number!")
                continue
        if board[row_list.index(row)][col_list.index(col)] != 0:
            row = None
            col = None
            print("Someone already put there!")
            continue
        else:
            c = 1
    coord = (row_list.index(row), col_list.index(col))
    return coord

def mark(move, main_board, player):
    board = main_board
    row = move[0]
    col = move[1]
    player_id = player
    board[row][col] = player_id
    return board

def print_board(x):
    board = copy.deepcopy(x)
    for i in range(len(x)):
        for y in range(len(x[i])):
            if x[i][y] == 0:
                board[i][y] = '.'
            elif x[i][y] == 1:
                board[i][y] = 'X'
            elif x[i][y] == 2:
                board[i][y] = 'O'
    print('   1   2   3')
    print("A", ' {:1} | {:1} | {:1}'.format(board[0][0], board[0][1], board[0][2]))
    print('  ---+---+---')
    print("B", ' {:1} | {:1} | {:1}'.format(board[1][0], board[1][1], board[1][2]))
    print('  ---+---+---')
    print("C", ' {:1} | {:1} | {:1}'.format(board[2][0], board[2][1], board[2][2]))
    return x





def has_won(board):
    winboard = board
    for i in range(len(winboard)):
        if winboard[i][0] == 1 and winboard[i][1] == 1 and winboard[i][2] == 1:
            return True, 1
        if winboard[i][0] == 2 and winboard[i][1] == 2 and winboard[i][2] == 2:
            return True, 2
        if winboard[0][i] == 1 and winboard[1][i] == 1 and winboard[2][i] == 1:
            return True, 1
        if winboard[0][i] == 2 and winboard[1][i] == 2 and winboard[2][i] == 2:
            return True, 2
    if winboard[0][0] == 1 and winboard[1][1] == 1 and winboard[2][2] == 1:
        return True, 1
    if winboard[0][0] == 2 and winboard[1][1] == 2 and winboard[2][2] == 2:
        return True, 2
    if winboard[0][2] == 1 and winboard[1][1] == 1 and winboard[2][0] == 1:
        return True, 1
    if winboard[0][2] == 2 and winboard[1][1] == 2 and winboard[2][0] == 2:
        return True, 2
    return False, 0

def is_full(board):
    fullboard = board
    if not 0 in fullboard[0] and not 0 in fullboard[1] and not 0 in fullboard[2]:
        return True
    else:
        return False

