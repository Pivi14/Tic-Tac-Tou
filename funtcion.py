def init_board():
    matrix = []
    for i in range(3):
        row = []
        matrix.append(row)
        for y in range(3):
            row.append(0)
    return matrix

def get_move():
    pass

def print_board():
    board = [[' ', '.', ' ', '|', ' ', '.', ' ', '|', ' ', '.', ' '], ['---+---+---']]
    print(*board[0], sep = '')
    for i in range(2):
        print(*board[1], '\n', *board[0], sep = '')

print_board()
