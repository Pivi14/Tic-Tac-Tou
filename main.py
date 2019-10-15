import function
import random

def main_menu():
    pass

y = random.randrange(1, 3)

def main():
    game = 0
    board = function.init_board()
    while game == 0:
        function.print_board(board)

main()