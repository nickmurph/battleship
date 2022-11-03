#
#
# GAME LOOP HELPER FUNCTIONS
#
#

import os
from bs_globalvars import *
import bs_playeractions
import bs_global_hub


def printPlayerBoard():
    game = bs_global_hub.get_game_pointer()
    playerBoard = game.playerBoard
    print("           YOUR AREA OF OPERATIONS         ")
    print("")
    print("    1   2   3   4   5   6   7   8   9   1O ")
    
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        if i == 0:
            print(*playerBoard[i], sep='  ')
        elif i == 1:
            print(*playerBoard[i], sep='  ', end='')
            print("                           KEY:")
        elif i == 2:
            print(*playerBoard[i], sep='  ', end='')
            print("                           AC = Aircraft Carrier")
        elif i == 3:
            print(*playerBoard[i], sep='  ', end='')
            print("                           BS = Battleship")
        elif i == 4:
            print(*playerBoard[i], sep='  ', end='')
            print("                           CR = Crusier")
        elif i == 5:
            print(*playerBoard[i], sep='  ', end='')
            print("                           SB = Submarine")
        elif i == 6:
            print(*playerBoard[i], sep='  ', end='')
            print("                           DT = Destroyer")
        elif i == 7:
            print(*playerBoard[i], sep='  ', end='')
            print("                           XX = Damaged Ship")
        elif i == 8:
            print(*playerBoard[i], sep='  ', end='')
            print("                           00 = Missed Shot")
        elif i == 9:
            print(*playerBoard[i], sep='  ', end='')
            print("                           ██ = Empty Ocean")
        else:
            print(*playerBoard[i], sep='  ')



def printPlayerBoardNoKey():
    # game = battleship.get_current_game()
    game = bs_global_hub.get_game_pointer()
    # game = main.get_bs_logic()
    playerBoard = game.playerBoard

    print("    1   2   3   4   5   6   7   8   9   1O ")
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        print(*playerBoard[i], sep='  ')



def printEnemyBoard():
    # game = battleship.get_current_game()
    game = bs_global_hub.get_game_pointer()
    enemyBoard = game.enemyBoard

    print("    1   2   3   4   5   6   7   8   9   1O ")
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        print(*enemyBoard[i], sep='  ')



def printTargetBoard():
    game = bs_global_hub.get_game_pointer()
    targetBoard = game.targetBoard

    print("       THE ENEMY'S AREA OF OPERATIONS      ")
    print("")
    print("    1   2   3   4   5   6   7   8   9   1O ")
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        if i == 1:
            print(*targetBoard[i], sep='  ', end='')
            print("                           KEY:")
        elif i == 2:
            print(*targetBoard[i], sep='  ', end='')
            print("                           XX = Successful Hit")
        elif i == 3:
            print(*targetBoard[i], sep='  ', end='')
            print("                           00 = Missed Shot")
        elif i == 4:
            print(*targetBoard[i], sep='  ', end='')
            print("                           ██ = Unknown Ocean")
        else:
            print(*targetBoard[i], sep='  ')





def input_spacer_with_board():
    print("")
    print("")
    printPlayerBoardNoKey()
    print("")
    print("")


def input_spacer_no_board():
    print("")
    print("")    

def clear_terminal():
    os.system('cls||clear')


def clear_and_print_both_boards():
    clear_terminal()
    input_spacer_no_board()
    input_spacer_no_board()
    print_ascii_logo()
    input_spacer_no_board()
    printPlayerBoard()
    input_spacer_no_board()
    printTargetBoard()
    input_spacer_no_board()

def print_both_boards():
    input_spacer_no_board()
    printPlayerBoard()
    input_spacer_no_board()
    printTargetBoard()
    input_spacer_no_board()

def print_ascii_logo():
   print( """

                ██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ 
                ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗
                ██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝
                ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ 
                ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     
                ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
                                                                                            
                """)



def print_ascii_game_over():
    print("""

                ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
                ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          
     """)


def print_welcome_screen():
    # clear_terminal()
    input_spacer_no_board()
    print_ascii_logo()
    input_spacer_with_board()


def print_stats_box():
    game = bs_global_hub.get_game_pointer()
    
    clear_terminal()
    print_ascii_logo()
    print(f"Turn Number: {game.turnCounter}")
    print(f"Player hits: {game.hitCounts[0]}")
    print(f"Enemy hits: {game.hitCounts[1]}")
    input_spacer_no_board()
    print(game.userLastTurnMessage)
    print(game.enemyLastTurnMessage)

def print_stats_and_both_boards():
    print_stats_box()
    print_both_boards()










