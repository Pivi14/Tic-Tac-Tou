import copy
board = [[1, 2, 2],[2, 2, 0],[2, 1, 0]]

def has_won(board):
    winboard = copy.deepcopy(board)
    for i in range(len(winboard)):
        if winboard[i][0] == 1 and winboard[i][1] == 1 and winboard[i][2] == 1:
            print(1)
            return True, 1
        if winboard[i][0] == 2 and winboard[i][1] == 2 and winboard[i][2] == 2:
            print(2)
            return True, 2
        if winboard[0][i] == 1 and winboard[1][i] == 1 and winboard[2][i] == 1:
            print(3)
            return True, 1
        if winboard[0][i] == 2 and winboard[1][i] == 2 and winboard[2][i] == 2:
            print(4)
            return True, 2
        if winboard[0][0] == 1 and winboard[1][1] == 1 and winboard[2][2] == 1:
            print(5)
            return True, 1
        if winboard[0][0] == 2 and winboard[1][1] == 2 and winboard[2][2] == 2:
            print(6)
            return True, 2
        if winboard[0][2] == 1 and winboard[1][1] == 1 and winboard[2][0] == 1:
            print(7)
            return True, 1
        if winboard[0][2] == 2 and winboard[1][1] == 2 and winboard[2][0] == 2:
            print(8)
            return True, 2
    return False

has_won(board)