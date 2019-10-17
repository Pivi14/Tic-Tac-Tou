from termcolor import *
import copy

board = [[1, 2, 0], [0, 2, 1], [1, 0, 0]]

def print_board(x):
    board = copy.deepcopy(x)
    for i in range(len(x)):
        for y in range(len(x[i])):
            if x[i][y] == 0:
                board[i][y] = '.'
            elif x[i][y] == 1:
                board[i][y] = colored('X', 'red')
            elif x[i][y] == 2:
                board[i][y] = colored('O', 'green')
    print('   1   2   3')
    print("A", ' {:1} | {:1} | {:1}'.format(board[0][0], board[0][1], board[0][2]))
    print('  ---+---+---')
    print("B", ' {:1} | {:1} | {:1}'.format(board[1][0], board[1][1], board[1][2]))
    print('  ---+---+---')
    print("C", ' {:1} | {:1} | {:1}'.format(board[2][0], board[2][1], board[2][2]))

print_board(board)
