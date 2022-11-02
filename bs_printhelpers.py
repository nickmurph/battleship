#
#
# GAME LOOP HELPER FUNCTIONS
#
#

import os
# from battleship import gameBoard, enemyBoard, targetBoard
# from battleship import turnCounter, hitCounts
from bs_globalvars import *
# from bs_enemyactions import enemyLastTurn
# from bs_playeractions import userLastTurn
# from battleship import get_current_game
import battleship
import bs_enemyactions
import bs_playeractions
import main



def printGameBoard():
    game = battleship.get_current_game()
    gameBoard = game.gameBoard
    print("           YOUR AREA OF OPERATIONS         ")
    print("")
    print("    1   2   3   4   5   6   7   8   9   1O ")
    
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        if i == 0:
            print(*gameBoard[i], sep='  ')
        elif i == 1:
            print(*gameBoard[i], sep='  ', end='')
            print("                           KEY:")
        elif i == 2:
            print(*gameBoard[i], sep='  ', end='')
            print("                           AC = Aircraft Carrier")
        elif i == 3:
            print(*gameBoard[i], sep='  ', end='')
            print("                           BS = Battleship")
        elif i == 4:
            print(*gameBoard[i], sep='  ', end='')
            print("                           CR = Crusier")
        elif i == 5:
            print(*gameBoard[i], sep='  ', end='')
            print("                           SB = Submarine")
        elif i == 6:
            print(*gameBoard[i], sep='  ', end='')
            print("                           DT = Destroyer")
        elif i == 7:
            print(*gameBoard[i], sep='  ', end='')
            print("                           XX = Damaged Ship")
        elif i == 8:
            print(*gameBoard[i], sep='  ', end='')
            print("                           00 = Missed Shot")
        elif i == 9:
            print(*gameBoard[i], sep='  ', end='')
            print("                           ██ = Empty Ocean")
        else:
            print(*gameBoard[i], sep='  ')



def printGameBoardNoKey():
    #game = battleship.get_current_game()
    game = main.get_bs_logic()
    gameBoard = game.gameBoard

    print("    1   2   3   4   5   6   7   8   9   1O ")
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        print(*gameBoard[i], sep='  ')



def printEnemyBoard():
    game = battleship.get_current_game()
    enemyBoard = game.enemyBoard

    print("    1   2   3   4   5   6   7   8   9   1O ")
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        print(*enemyBoard[i], sep='  ')



def printTargetBoard():
    game = battleship.get_current_game()
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
    printGameBoardNoKey()
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
    printGameBoard()
    input_spacer_no_board()
    printTargetBoard()
    input_spacer_no_board()

def print_both_boards():
    input_spacer_no_board()
    printGameBoard()
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


def clear_and_print_welcome_screen():
    clear_terminal()
    input_spacer_no_board()
    print_ascii_logo()
    input_spacer_with_board()


def print_stats_box():
    game = battleship.get_current_game()
    
    clear_terminal()
    print_ascii_logo()
    print(f"Turn Number: {game.turnCounter}")
    print(f"Player hits: {game.hitCounts[0]}")
    print(f"Enemy hits: {game.hitCounts[1]}")
    input_spacer_no_board()
    print(bs_playeractions.userLastTurn)
    print(bs_enemyactions.enemyLastTurn)








