
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


def testhelperfunc(num):
    print("blerp" + str(num))



gameBoard = []
enemyBoard = []
targetBoard = []
for x in range(10):
    gameBoard.append(['██']*10)
    enemyBoard.append(['__']*10)
    targetBoard.append(['__']*10)



# for x in range(0,5):
#     gameBoard[x][0] = 'X'
#     print(x,0)

# print("""

# ██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ 
# ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗
# ██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝
# ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ 
# ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     
# ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
                                                                             
# """)

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

print("")
print("")
print("")
print("")
#printGameBoard()


gameBoard[0][0] = 'AC'
gameBoard[0][1] = 'AC'
gameBoard[0][2] = 'AC'
gameBoard[0][3] = 'AC'
gameBoard[0][4] = 'AC'


gameBoard[1][7] = 'BS'
gameBoard[2][7] = 'BS'
gameBoard[3][7] = 'BS'
gameBoard[4][7] = 'BS'


gameBoard[5][4] = 'CR'
gameBoard[5][5] = 'CR'
gameBoard[5][6] = 'CR'


gameBoard[7][0] = 'SB'
gameBoard[7][1] = 'SB'
gameBoard[7][2] = 'SB'


gameBoard[9][7] = 'DT'
gameBoard[9][8] = 'DT'



enemyBoard[0][4] = 'XX'
enemyBoard[0][5] = 'XX'
enemyBoard[0][6] = 'XX'
enemyBoard[0][7] = 'XX'
enemyBoard[0][8] = 'XX'
enemyBoard[2][4] = '00'



targetBoard[0][4] = 'XX'
targetBoard[0][5] = 'XX'
targetBoard[0][6] = 'XX'
targetBoard[0][7] = '██'
targetBoard[0][8] = '██'
targetBoard[2][4] = '██'
printGameBoard()
# print("")
# print("")
# print("")
# print("")
# printEnemyBoard()
print("")
print("")
print("")
print("")
printTargetingBoard()
print("")
print("")






# For AI placement
# Give player option to randomize as well?
# generate pairs of tuples (beg, end)
# Randomly select one of those pairs for first ship and add it to the board
# Randomly select next pair, checking that theres no overlap
# worth considering refactoring for future speed improvements
        # check if beg and end empty first
        # if so use generate full funct and check those? O(1) to check any coordinate, and generate full is at most O(5)
        # using a hash map might better if board was theoretically infinite but there are hard limits for now
        # if the board is made dynamically resizable in future iteration and larger ships added there still won't be any lengths over 10 so "O(n)" means far less here

def generate_valid_horizontal_placements(shipSize):
    shipSizeOffset = shipSize -1
    validHorzList = []
    for row in range(10):
        for col in range(10):
            if col+shipSizeOffset < 10:
                #print(str(row) + "," + str(col) + ",  " + str(row) +","+ str(col+shipSizeOffset))
                begTuple = (row,col)
                endTuple = (row, col+shipSizeOffset)
                validHorzList.append((begTuple, endTuple))
        #print("")
    return validHorzList

def generate_valid_vertical_placements(shipSize):
    shipSizeOffset = shipSize -1
    validVertList = []
    for col in range(10):
        for row in range(10):
            if row+shipSizeOffset < 10:
                #print(str(row) + "," + str(col) + ",  " + str(row+shipSizeOffset) +","+ str(col))
                begTuple = (row,col)
                endTuple = (row+shipSizeOffset, col)
                validVertList.append((begTuple,endTuple))
        #print("")
    return validVertList


#generate_valid_horizontal_placements(5)
#generate_valid_vertical_placements(5)


#print("█")


#print(str(gameBoard[0]))
#print(' '.join(gameBoard[0]))



def generate_AI_placement(shipSize):
    validHorzPlacements = generate_valid_horizontal_placements(shipSize)
    validVertPlacements = generate_valid_vertical_placements(shipSize)
    totalPossibilities = len(validHorzPlacements) + len (validVertPlacements)
    randNum = int(random.uniform(0, totalPossibilities-1))
    randPair = None
    if randNum < len(validHorzPlacements):
        randPair = validHorzPlacements[randNum]
    else:
        randPair = validVertPlacements[randNum-len(validHorzPlacements)]
    #print(randPair)





#generate_AI_placement(5)

# carrierPlacementsH = generate_valid_vertical_placements(5)
# print(len(carrierPlacementsH))
# print(carrierPlacementsH[0])
# print(carrierPlacementsH[0][0])
# print(carrierPlacementsH[0][0][0])



