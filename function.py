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
    while board[a.index(row)][b.index(col)] != 0:
        while not row in a:
            try:
                row = input("Give me the row's letter: ").upper()
            except:
                continue
        while not col in b:
            try:
                col = int(input("Give me the column's number: "))
            except:
                continue
    coord = (row, col)
    return coord

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