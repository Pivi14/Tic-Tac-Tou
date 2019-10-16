import sys
from art import *
from termcolor import colored, cprint
text=text2art('Tic', font='broadway',chr_ignore=True)
text2=text2art('Tac', font='broadway',chr_ignore=True)
text3=text2art('Tou', font='broadway',chr_ignore=True)
cprint(text, "red", attrs=["bold"], )
cprint(text2, "white", attrs=["bold"])
cprint(text3, "green", attrs=["bold"])
cprint("by In 2 Calories\n", "cyan", attrs=["bold"])