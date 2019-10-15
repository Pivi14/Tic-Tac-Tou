import function
import random

def main_menu():
    print('MENU')
    print('(1) Player vs Player')
    a = input("Give me the menu's number: ")
    if a == 1:
        game = 1
    return game


def main():
    y = 1
    game = 5
    board = function.init_board()
    while game == 0:
        function.print_board(board)
        board = function.mark()

main_menu()
main()