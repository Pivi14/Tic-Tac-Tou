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
        function.print_board(board)
        coord = function.get_move(board)
        function.mark(coord, board, player)
        if player == 1:
            player = 2
        elif player == 2:
            player = 1
        win = function.has_won(board)# innentől lefele van az a rész, ahol implementáltam a függvényeidet
        if win[0]:
            if win[1] == 1:
                function.print_board(board)
                print('Player1 is the winner')
                game = 1
            elif win[1] == 2:
                function.print_board(board)
                print('Player2 is the winner')
                game = 1
        draw = function.is_full(board)
        if draw:
            function.print_board(board)
            print('The table is full, and the game is draw!')
            game = 1
# ha gondolod próbáld ki. az alapok működnek

if __name__ == '__main__':
    main()
