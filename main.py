import function

def main():
    game = 5
    print('MENU')
    print('(1) Player vs Player')
    a = int(input("Give me the menu's number: "))
    if a == 1:
        game = 0
    board = function.init_board()
    while game == 0:
        function.print_board(board)
        coord = function.get_move()
        function.mark(coord, board)




if __name__ == '__main__':
    main()
