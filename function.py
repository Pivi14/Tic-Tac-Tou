def init_board():
    matrix = []
    for i in range(3):
        row = []
        matrix.append(row)
        for y in range(3):
            row.append(0)
    return matrix

def get_move():
    board = init_board()
    a = ['A', 'B', 'C']
    b = [1, 2, 3]
    row = None
    col = None
    c = 0
    while c == 0:
        while not row in a:
            try:
                row = input("Give me the row's letter A, B or C: ").upper()
            except:
                print("Please enter a valid letter!")
                continue
        while not col in b:
            try:
                col = int(input("Give me the column's number 1, 2, or 3: "))
            except:
                print("Please enter a valid number!")
                continue
        if board[a.index(row)][b.index(col)] != 0:
            row = None
            col = None
            print("Someone already put there!")
            continue
        else:
            c = 1
    coord = (a.index(row), b.index(col))
    return coord

def mark(move, main_board):
    board = main_board
    a = move[0]
    b = move[1]
    y = 1
    board[a][b] = y
    if y == 1:
        y = 2
    else:
        y = 1
    return board, y

def print_board(x):
    board = x
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





def has_won():
    winboard=init_board()

    for i in range(len(winboard)):
        if winboard[i][0]==1 and winboard[i][1] == 1 and winboard[i][2] == 1:
            return True
        if winboard[i][0] == 2 and winboard[i][1] ==2 and winboard[i][2] == 2:
            return True
        if winboard[0][i] ==1 and winboard[1][i] == 1 and winboard[2][i] == 1:
            return True
        if winboard[0][i] == 2 and winboard[1][i] == 2 and winboard[2][i] == 2:
            return True
    return False




def is_full():
    fullboard=init_board()
    if not 0 in fullboard[0] and not 0 in fullboard[1] and not 0 in fullboard[2]:
        return True
    else:
        return False

get_move()
