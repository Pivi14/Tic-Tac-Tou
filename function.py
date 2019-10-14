def init_board():
    matrix = []
    for i in range(3):
        row = []
        matrix.append(row)
        for y in range(3):
            row.append(0)
    board = matrix
    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            if matrix[i][y] == 0:
                board[i][y] = '.'
            elif matrix[i][y] == 1:
                board[i][y] = 'X'
            elif matrix[i][y] == 2:
                board[i][y] = 'O'
    return board

def get_move():
    row = None
    col = None
    while row == 'A' or 'B' or 'C':
        try:
            row = input("Give me the row's letter: ").upper()
        except:
            continue
    while col == 1 or 2 or 3:
        try:
            col = int(input("Give me the column's number: "))
        except:
            continue
    coord = (row, col)
    return coord

def print_board(board):
    print('   1   2   3')
    print("A", ' {:1} | {:1} | {:1}'.format(board[0][0], board[0][1], board[0][2]))
    print('  ---+---+---')
    print("B", ' {:1} | {:1} | {:1}'.format(board[1][0], board[1][1], board[1][2]))
    print('  ---+---+---')
    print("C", ' {:1} | {:1} | {:1}'.format(board[2][0], board[2][1], board[2][2]))
