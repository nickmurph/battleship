#
#
# GAME LOOP HELPER FUNCTIONS
#
#

import os
# from battleship import gameBoard, enemyBoard, targetBoard
# from battleship import turnCounter, hitCounts
from bs_globalvars import *
from bs_enemyactions import enemyLastTurn
from bs_playeractions import userLastTurn



def printGameBoard():
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
    print("    1   2   3   4   5   6   7   8   9   1O ")
    
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        print(*gameBoard[i], sep='  ')

def printEnemyBoard():
    print("    1   2   3   4   5   6   7   8   9   1O ")
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        print(*enemyBoard[i], sep='  ')



def printTargetBoard():
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




def print_stats_box():
    clear_terminal()
    print_ascii_logo()
    print(f"Turn Number: {turnCounter}")
    print(f"Player hits: {hitCounts[0]}")
    print(f"Enemy hits: {hitCounts[1]}")
    input_spacer_no_board()
    print(userLastTurn)
    print(enemyLastTurn)








