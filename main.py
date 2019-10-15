import function

def main():
    game = 5
    print('MENU')
    print('(1) Player vs Player')
    a = int(input("Give me the menu's number: "))
    if a == 1:
        game = 0
    board = function.init_board()
    player = 1
    while game == 0:
        print(board)
        old_board = function.print_board(board)
        print(old_board)
        coord = function.get_move(board)
        function.mark(coord, board, player)
        if player == 1:
            player = 2
        elif player == 2:
            player = 1




if __name__ == '__main__':
    main()
