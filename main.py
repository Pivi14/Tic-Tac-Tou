import function
from art import *
from termcolor import colored, cprint
import os
from ai import *
import time


def main_menu():
    text=text2art('Tic', font='broadway',chr_ignore=True)
    text2=text2art('Tac', font='broadway',chr_ignore=True)
    text3=text2art('Tou', font='broadway',chr_ignore=True)
    cprint(text, "red", attrs=["bold"], )
    cprint(text2, "white", attrs=["bold"])
    cprint(text3, "green", attrs=["bold"])
    cprint("by In 2 Calories\n", "cyan", attrs=["bold"])
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
    player = 1
    win1 = text2art(Nam1 + ' is the winner')
    win2 = text2art(Nam2 + 'is the winner')
    play_draw = text2art('Draw')
    while play == 1:
        game = 1
        board = function.init_board()
        while game == 1:
            os.system('clear')
            function.print_board(board)
            if player == 1:
                print('The next is ' + Nam1)
            else:
                print('The next is ' + Nam2)
            coord = function.get_move(board)
            function.mark(coord, board, player)
            if player == 1:
                player = 2
            else:
                player = 1
            win = function.has_won(board)
            if win[0]:
                if win[1] == 1:
                    os.system('clear')
                    function.print_board(board)
                    cprint(win1, color='red', attrs=['bold'])
                    replay = input('Are you replay? y or n: ')
                    if replay == 'y':
                        player = 2
                        game = 0
                        continue
                    elif replay == 'n':
                        play = 0
                    game = 0
                elif win[1] == 2:
                    os.system('clear')
                    function.print_board(board)
                    cprint(win2, color='green', attrs=['bold'])
                    replay = input('Are you replay? y or n: ')
                    if replay == 'y':
                        player = 1
                        game = 0
                        continue
                    elif replay == 'n':
                        play = 0
                    game = 0
            draw = function.is_full(board)
            if game == 1:
                if draw:
                    os.system('clear')
                    function.print_board(board)
                    print(play_draw)
                    replay = input('Are you replay? y or n: ')
                    if replay == 'y':
                        game = 0
                        continue
                    elif replay == 'n':
                        play = 0
                    game = 0


def PvA():
    Nam1 = input("Player1's name? ")
    play = 1
    win1 = text2art(Nam1 + ' is the winner')
    win2 = text2art('Computer is the winner')
    play_draw = text2art('Draw')
    ai = input('Choose the difficult (E - easy or H - hard): ').upper()
    while play == 1:
        player = 1
        game = 1
        board = function.init_board()
        while game == 1:
            os.system('clear')
            function.print_board(board)
            if player == 1:
                print('The next is ' + Nam1)
                coord = function.get_move(board)
            else:
                print('The next is the Computer')
                time.sleep(1)
                coord = ai_move(board, ai)
                print(coord)
            function.mark(coord, board, player)
            if player == 1:
                player = 2
            else:
                player = 1
            win = function.has_won(board)
            if win[0]:
                if win[1] == 1:
                    os.system('clear')
                    function.print_board(board)
                    cprint(win1, color='red', attrs=['bold'])
                    replay = input('Are you replay? y or n: ')
                    if replay == 'y':
                        game = 0
                        continue
                    elif replay == 'n':
                        play = 0
                    game = 0
                elif win[1] == 2:
                    os.system('clear')
                    function.print_board(board)
                    cprint(win2, color='green', attrs=['bold'])
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
                    os.system('clear')
                    function.print_board(board)
                    print(play_draw)
                    replay = input('Are you replay? y or n: ')
                    if replay == 'y':
                        game = 0
                        continue
                    elif replay == 'n':
                        play = 0
                    game = 0

def AvA():
    aieasy = 'E'
    aihard = 'H'
    play = 1
    win1 = text2art('Easy AI is the winner')
    win2 = text2art('Hard AI is the winner')
    play_draw = text2art('Draw')
    while play == 1:
        player = 1
        game = 1
        board = function.init_board()
        while game == 1:
            os.system('clear')
            function.print_board(board)
            if player == 1:
                print('The next is the Easy AI')
                time.sleep(1)
                coord = ai_move(board, aieasy)
            else:
                print('The next is the Hard AI')
                time.sleep(1)
                coord = ai_move(board, aihard)
                print(coord)
            function.mark(coord, board, player)
            if player == 1:
                player = 2
            else:
                player = 1
            win = function.has_won(board)
            if win[0]:
                if win[1] == 1:
                    os.system('clear')
                    function.print_board(board)
                    cprint(win1, color='red', attrs=['bold'])
                    replay = input('Are you replay? y or n: ')
                    if replay == 'y':
                        game = 0
                        continue
                    elif replay == 'n':
                        play = 0
                    game = 0
                elif win[1] == 2:
                    os.system('clear')
                    function.print_board(board)
                    cprint(win2, color='green', attrs=['bold'])
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
                    os.system('clear')
                    function.print_board(board)
                    print(play_draw)
                    replay = input('Are you replay? y or n: ')
                    if replay == 'y':
                        game = 0
                        continue
                    elif replay == 'n':
                        play = 0
                    game = 0

if __name__ == '__main__':
    os.system('clear')
    prog = 1
    while prog == 1:
        os.system('clear')
        game = main_menu()
        if game == 1:
            PvP()
        elif game == 2:
            PvA()
        elif game == 3:
            AvA()
        elif game == 4:
            prog = 0
    os.system('clear')
    byetext=text2art("Good bye\n see you soon!", font='broadway', chr_ignore=True)
    cprint(byetext, 'yellow', attrs=['bold'])