
import random
import colorama
from colorama import Fore, Style, init


colorama.init(convert=True)


test_color = Fore.RED + 'O' + Style.RESET_ALL
print(test_color)

test_color2 = f'{Fore.GREEN}X{Style.RESET_ALL}'
print(test_color2)
print(Fore.LIGHTWHITE_EX + 'THIS IS WHAT THIS COLOR LOOKS LIKE' + Style.RESET_ALL)
print(Fore.YELLOW + 'THIS IS WHAT THIS COLOR LOOKS LIKE' + Style.RESET_ALL)
print(Fore.MAGENTA + 'THIS IS WHAT THIS COLOR LOOKS LIKE' + Style.RESET_ALL)
print(Fore.BLACK + 'THIS IS WHAT THIS COLOR LOOKS LIKE' + Style.RESET_ALL)
print(Fore.BLUE + 'THIS IS WHAT THIS COLOR LOOKS LIKE' + Style.RESET_ALL)
print(Fore.CYAN + 'THIS IS WHAT THIS COLOR LOOKS LIKE' + Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + 'THIS IS WHAT THIS COLOR LOOKS LIKE' + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + 'THIS IS WHAT THIS COLOR LOOKS LIKE' + Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX + 'THIS IS WHAT THIS COLOR LOOKS LIKE' + Style.RESET_ALL)




# openSea = Fore.GREEN + '__' + Style.RESET_ALL
# shipBody = 'QQ'
# shipStruck = Fore.RED + 'XX' + Style.RESET_ALL
# missedShot = Fore.YELLOW + '00' + Style.RESET_ALL

def testhelperfunc(num):
    print("blerp" + str(num))



gameBoard = []
enemyBoard = []
targetBoard = []
for x in range(10):
    gameBoard.append(['██']*10)
    enemyBoard.append(['__']*10)
    targetBoard.append(['__']*10)


# original board print function
# def printGameBoard():
#     for i in range(10):
#         if i == 0:
#             print("    1    2    3    4    5    6    7    8    9    1O ")
#         curLetter = chr(i+65)
#         print(curLetter + " " + str(gameBoard[i]))

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
            





boardPrintHashMap = {}
boardPrintHashMap[1] = "                           KEY:"
boardPrintHashMap[2] = "                           AC = Aircraft Carrier"
boardPrintHashMap[3] = "                           BS = Battleship"
boardPrintHashMap[4] = "                           CR = Crusier"
boardPrintHashMap[5] = "                           SB = Submarine"
boardPrintHashMap[6] = "                           DT = Destroyer"
boardPrintHashMap[7] = "                           XX = Damaged Ship"
boardPrintHashMap[8] = "                           00 = Missed Shot"
boardPrintHashMap[9] = "                           ██ = Empty Ocean"



def printGameBoardNoKey():
    print("    1   2   3   4   5   6   7   8   9   1O ")
    
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        print(*gameBoard[i], sep='  ', end="")
        print(boardPrintHashMap[i])


def printGameBoard2():
    print("           YOUR AREA OF OPERATIONS         ")
    print("")
    print("    1   2   3   4   5   6   7   8   9   1O ")
    
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        print(*gameBoard[i], sep='  ')
        print()





def printEnemyBoard():
    print("    1   2   3   4   5   6   7   8   9   1O ")
    for i in range(10):
        curLetter = chr(i+65)
        print(curLetter + "   ", end="")
        print(*enemyBoard[i], sep='  ')


def printTargetingBoard():
    print("       THE ENEMY'S AREA OF OPERATIONS      ")
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



testSquare = Fore.YELLOW + '00' + Style.RESET_ALL
def updateGivenBoard(board):
    board[0][0] = testSquare


updateGivenBoard(targetBoard)
printTargetingBoard()




# print("LAST TURN RESULTS: ")
# print(userLastTurn)
# print(enemyLastTurn)

def update_user_last_turn(outcome, coord):
    if outcome == "hit":
        userLastTurn = "HIT! You struck an enemy ship at {coord}!"
    else:
        userLastTurn = f"YOU MISSED! No enemy ship at {coord}!"

def update_enemy_last_turn(outcome, coord):
    if outcome == "hit":
        enemyLastTurn = f"HIT! The enemy struck your ship at {coord}!"
    else:
        enemyLastTurn = f"THE ENEMY MISSED! Their shot landed harmlessly at {coord}!"




shipsHashMap = {}
shipsHashMap['Carrier'] = 5, Fore.GREEN + 'AC' + Style.RESET_ALL
shipsHashMap['Battleship'] = 4, Fore.GREEN + 'BS' + Style.RESET_ALL
shipsHashMap['Cruiser'] = 3, Fore.GREEN + 'CR' + Style.RESET_ALL
shipsHashMap['Submarine'] = 3, Fore.GREEN + 'SB' + Style.RESET_ALL
shipsHashMap['Destroyer'] = 2, Fore.GREEN + 'DT' + Style.RESET_ALL


testKeys = shipsHashMap.keys()
#print(testKeys[0])

listKeys = list(shipsHashMap.keys())
print(listKeys[0])

print(next(iter(shipsHashMap)))

for i in range(5):
    print(listKeys[i])
 

shipNameList = list(shipsHashMap.keys())



# For auto placement
# worth considering refactoring for future speed improvements
        # check if beg and end empty first
        # if so use generate full funct and check those? O(1) to check any coordinate, and generate full is at most O(5)
        # using a hash map might better if board was theoretically infinite but there are hard limits for now
        # if the board is made dynamically resizable in future iteration and larger ships added there still won't be any lengths over 10 so "O(n)" means far less here

