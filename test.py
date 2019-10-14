board = [[0, 0, 1], [1, 2, 1], [1, 0, 2]]
def get_move():
    global board
    a = ['A', 'B', 'C']
    b = [1, 2, 3]
    row = None
    col = None
    c = 0
    while c == 0:
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
        if board[a.index(row)][b.index(col)] != 0:
            continue
        else:
            c = 1
    coord = (row, col)
    return coord

get_move()