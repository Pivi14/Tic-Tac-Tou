import function

def main_menu():
    gameplay = 0
    print('MENU')
    print(' (1) Player vs Player\n', '(2) Player vs AI\n', '(3) Ai vs Ai\n', '(4) Exit')
    a = int(input("Give me the menu's number: "))
    if a == 1:
        gameplay = 1
    elif a == 2:
        gameplay = 2
    elif a == 3:
        gameplay = 3
    elif a == 4:
        gameplay = 4
    return gameplay

def PvP():
    Nam1 = input("Player1's name? ")
    Nam2 = input("Player2's name? ")
    play = 1
    while play == 1:
        game = 1
        board = function.init_board()
        player = 1
        while game == 1:
            function.print_board(board)
            if player == 1:
                print('The next is ' + Nam1)
            else:
                print('The nest is ' + Nam2)
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
                    print(Nam1 + ' is the winner')
                    replay = input('Are you replay? y or n: ')
                    if replay == 'y':
                        game = 0
                        continue
                    elif replay == 'n':
                        play = 0
                    game = 0
                elif win[1] == 2:
                    function.print_board(board)
                    print(Nam2 + ' is the winner')
                    replay = input('Are you replay? y or n: ')
                    if replay == 'y':
                        game = 0
                        continue
                    elif replay == 'n':
                        play = 0
                    game = 0
            draw = function.is_full(board)
            if game == 1:
                if draw:
                    function.print_board(board)
                    print('The table is full, and the game is draw!')
                    replay = input('Are you replay? y or n: ')
                    if replay == 'y':
                        game = 0
                        continue
                    elif replay == 'n':
                        play = 0
                    game = 0

def PvA():
    pass

def AvA():
    pass

if __name__ == '__main__':
    prog = 1
    while prog == 1:
        game = main_menu()
        if game == 1:
            PvP()
        elif game == 2:
            PvA()
        elif game == 3:
            AvA()
        elif game == 4:
            prog = 0
    print('Good bye!')