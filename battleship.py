import random
import os
import colorama
from colorama import Fore, Style, init



colorama.init(convert=True)



# TO DO LIST

# break battleship.py up into several smaller files based on function categories

# logic for registering sinkings of specific vessels, announcing to the player

# fix crashing on incorrect user inputs

# develop further AI models as outlined in notes

# AI levels: Hapless Seaman, Admiral Nelson, Fleet Admiral Nimitz
# # Hapless Seaman: This man would be out of his depth commanding a tugboat. 
# # Happy will give random fire orders while cowering beneath deck.
# #
# # Admiral Nelson: Nelson's victory over the French was legendary, but he commanded vessels far less advanced than those present today. 
# # Nelson will intelligently consider firing solutions based on previous hits and misses.
# #
# # Fleet Admiral Nimitz: The greatest admiral of WW2, and the last to hold the title of Fleet Admiral. 
# # Nimitz will offer you the toughest challenge of all (more advanced logic re: traversing the grid, future implementation of remembering player tendencies?)


# consider refactoring hardcoded 10x10 grid and corresponding logic (eg, checking if, for grid coordinate x, 0 >= x <= 9) into a gridSize variable
# this will allow for arbitrarily scaling the battleship board if a future feature with different grid sizes is implemented


# player/profile framework of some sort
# # - username/password good excuse to demonstrate proper implementation of password hashing/data storage, lays foundation for eventual GUI version
# # - having player profiles would also allow for the tracking of tendencies -> future implementation of learning (or at least remembering) AI


# eventual GUI extension, which will require some refactoring

# consider how much refactoring would be needed to implement an option to play SALVO:
# # Salvo is a variant on Battleship, with the following rule changes described by the official Milton Bradley instructions
# # each player fires 5 shots per turn instead of 1
# # if a player loses a ship, they fire one less shot per turn (ie, each surviving ship in the players fleet is firing once per turn)
# # an even more challenging version of Salvo involves not announcing which of your ships is hit
#




#
#
# GRID CREATION AND PRINTING, HASHMAP FOR SHIP LENGTHS
#
# ██
gameBoard = []
enemyBoard = []
targetBoard = []
openSea = Fore.LIGHTCYAN_EX + '__' + Style.RESET_ALL
shipBody = Fore.GREEN + 'QQ' + Style.RESET_ALL
shipStruck = Fore.RED + 'XX' + Style.RESET_ALL
missedShot = Fore.LIGHTCYAN_EX + '00' + Style.RESET_ALL
userTargets = []
enemyTargets = []
hitCounts = [0,0]
enemyGridStartPos = [0,-1]
#enemyGridStartPos = generate_random_target()

# hash map for retrieving size of ships with their name as a key
shipsHashMap = {}
shipsHashMap['Carrier'] = 5, Fore.GREEN + 'AC' + Style.RESET_ALL
shipsHashMap['Battleship'] = 4, Fore.GREEN + 'BS' + Style.RESET_ALL
shipsHashMap['Cruiser'] = 3, Fore.GREEN + 'CR' + Style.RESET_ALL
shipsHashMap['Submarine'] = 3, Fore.GREEN + 'SB' + Style.RESET_ALL
shipsHashMap['Destroyer'] = 2, Fore.GREEN + 'DT' + Style.RESET_ALL

shipNameList = list(shipsHashMap.keys())



for x in range(10):
    gameBoard.append([openSea]*10)
    enemyBoard.append([openSea]*10)
    targetBoard.append([openSea]*10)




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




#
#
# GRID RELATED HELPER FUNCTIONS
#
#

# Returns True if two x,y tuples are in the same row
def in_same_row(beg, end):
    return beg[0] == end[0]
# Returns True if two x,y tuples are in the same column 
def in_same_column(beg, end):
    return beg[1] == end[1]

# Returns the difference between the row(1st) value of end and beg
def get_row_diff(beg,end):
    return end[0]-beg[0]
# Returns the difference between the col(2nd) value of end and beg
def get_col_diff(beg,end):
    return end[1]-beg[1]

# Returns true if the first values of beg and end are within the bounds of the grid
def valid_row_bounds(beg,end):
    return beg[0] >= 0 and end[0] <= 9
# Returns true if the second values of beg and end are within the bounds of the grid
def valid_col_bounds(beg,end):
    return beg[1] >= 0 and end[1] <= 9

# take in two tuples, begin and end, and return all of the coordinates contained between those two points along x or y axis
def generate_full_coords(beg, end):
    full_coords = []
    if get_col_diff(beg,end) == 0:
        for i in range(beg[0], end[0]+1):
            full_coords.append((i, beg[1]))
    elif get_row_diff(beg,end) == 0:
        for i in range(beg[1], end[1]+1):
            full_coords.append((beg[0],i))
    return full_coords

#returns True if the coordinate sent as an argument already has a ship occupying it on the board
def square_occupied(board, grid_tuple):
    return board[grid_tuple[0]][grid_tuple[1]] != openSea

def coords_occupied(board, full_coords):
    flag = False
    for coord in full_coords:
        if square_occupied(board, coord):
            flag = True
            #print("This coordinate, " + str(coord) + ", is already occupied!")
    return flag



# 
# Places a ship on the grid in the squares between beg and end
# ARGS: string, tuple, tuple
# 
def place_ship(board, shipName, beg, end):
    shipLength = shipsHashMap[shipName][0]
    shipBody = shipsHashMap[shipName][1]

    #this is a placement from left to right along a row, with beg as the left coordinates
    if in_same_row(beg,end) and get_col_diff(beg,end) == shipLength-1 and valid_col_bounds(beg,end):
        potential_coords = generate_full_coords(beg,end)
        if coords_occupied(board, potential_coords) != True:
            for i in range(shipLength):
                board[beg[0]][beg[1]+i] = shipBody

    #this is a placement from top to bottom along a column, with beg as the top coordinates
    elif in_same_column(beg,end) and get_row_diff(beg,end) == shipLength-1 and valid_row_bounds(beg,end):
        potential_coords = generate_full_coords(beg,end)
        if coords_occupied(board, potential_coords) != True:
            for i in range(shipLength):
                board[beg[0]+i][beg[1]] = shipBody
    else:
        return False



#
#
# USER INPUT AND AXIS CONVERSION HELPER FUNCTIONS
#
#

def letter_to_ord(ltr):
    if len(ltr) != 1:
        raise Exception("Letter string larger than 1")
    elif ord(ltr) >= 65 and ord(ltr) < 75:
        return ord(ltr)
    else:
        raise Exception("Letter outside acceptable ord range")

def ord_to_letter(num):
    if num >= 65 and num < 75:
        return chr(num)
    else:
        raise Exception("Letter outside acceptable ord range")

def ord_to_grid_num(ordnum):
    return ordnum-65

def grid_num_to_ord(gridNum):
    return gridNum+65

def is_valid_alphanum(inputStr):
    if type(inputStr) != type(""):
        return False
    elif len(inputStr) not in range(2,4):
        return False
    elif inputStr[0] not in "ABCDEFGHIJ":
        return False
    elif int(inputStr[1]) not in range(1,11):
        return False
    elif len(inputStr) == 3 and int(inputStr[1] + inputStr[2]) not in range (1,11):
        return False
    else:
        return True


def process_alphanum_to_coord(user_coord):
    try:
        row = user_coord[0]
        if len(user_coord) == 2:
            col = int(user_coord[1])
        elif len(user_coord) == 3:
            col = int(user_coord[1] + user_coord[2])

        if len(user_coord) not in range(2,4):
            raise Exception("User coordinate improper length")
        
        elif letter_to_ord(row) != 0 and col in range(1,11):
            row = letter_to_ord(row)
            row = ord_to_grid_num(row)
            col = col -1
            return (row, col)
        else:
            raise Exception("Either row or column input not acceptable")
    except:
        return False

def coord_to_alphanumeric(coord):
    row = coord[0]
    col = coord[1]
    row = grid_num_to_ord(row)
    row = ord_to_letter(row)
    col += 1
    return row + (str(col))




#
#
# GAME LOOP HELPER FUNCTIONS
#
#

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




def ship_input_loop(shipName):
    if shipName == "Carrier":
        print("Your first ship is a " + shipName + ", " + str(shipsHashMap[shipName][0]) + " squares long.")
    else:
        print("Your next ship is a " + shipName + ", " + str(shipsHashMap[shipName][0]) + " squares long.")
    
    shipLoop = True
    while shipLoop:
        inputBeg = input("Type the beginning coordinate: ")
        while not is_valid_alphanum(inputBeg):
            inputBeg = input("Invalid coordinate. Type a valid beginning coordinate, of the form [A-J][1-10]: ")
        inputEnd = input("Type the ending coordinate: ")
        while not is_valid_alphanum(inputEnd):
            inputEnd = input("Invalid coordinate. Type a valid ending coordinate, of the form [A-J][1-10]: ")

        inputBeg = process_alphanum_to_coord(inputBeg)
        inputEnd = process_alphanum_to_coord(inputEnd)

        if place_ship(gameBoard, shipName, inputBeg, inputEnd) != False:
            shipLoop = False
        else:
            print("The coordinates you chose were sized improperly or occupied!")
            print(f"try again with coordinates {shipsHashMap[shipName][0]} spaces apart, vertically or horizontally.")



def player_manual_turn_input():
    print("It is your turn. Pick a square on the grid to target, of the form [A-J][1-10].")
    print("For Example, to target the uppermost left corner, type A1.")

    gridTarget = None
    rowTarget = None
    colTarget = None
    userFindingTarget = True

    while userFindingTarget:
        inputTarget = input("Type the coordinate you want to target: ")
        gridTarget = process_alphanum_to_coord(inputTarget)
        if gridTarget == False:
            print("The given input was not a valid coordinate.")
            continue
        rowTarget = gridTarget[0]
        colTarget = gridTarget[1]

        if gridTarget in userTargets:
            print("You have already entered this target, choose another.")
        else:
            userTargets.append(gridTarget)
            if enemyBoard[rowTarget][colTarget] == openSea:
                targetBoard[rowTarget][colTarget] = missedShot
                print("")
                global userLastTurn
                userLastTurn = f"YOU MISSED! No enemy ship at {inputTarget}!"
            else:
                targetBoard[rowTarget][colTarget] = shipStruck
                hitCounts[0] = hitCounts[0] + 1
                print("")
                userLastTurn = f"YOU SCORED A HIT! Enemy ship struck at {inputTarget}!"
            userFindingTarget = False

def player_auto_turn_input():
    randomTarget = None
    randRow = None
    randCol = None
    userAutoFindingTarget = True
    while userAutoFindingTarget:
        randomTarget = generate_random_target()
        randRow = randomTarget[0]
        randCol = randomTarget[1]
        if randomTarget not in userTargets:
            userTargets.append(randomTarget)
            userAutoFindingTarget = False
    if enemyBoard[randRow][randCol] == openSea:
        targetBoard[randRow][randCol] = missedShot
        alphaRandMiss = coord_to_alphanumeric(randomTarget)
        global userLastTurn
        userLastTurn = f"YOU MISSED! No enemy ship at {alphaRandMiss}!"
        print("")
        print("")
    else:
        targetBoard[randRow][randCol] = shipStruck
        alphaRandHit = coord_to_alphanumeric(randomTarget)
        hitCounts[0] = hitCounts[0] + 1
        userLastTurn = f"YOU SCORED A HIT! Enemy ship struck at {alphaRandHit}!"
        print("")
        print("")

#currentPos is a tuple of 
def traverseGrid(currentPos, leftOrRight, upOrDown, jumpInterval):
    nextTarget = currentPos
    colDirection = leftOrRight
    rowDirection = upOrDown
    jump = jumpInterval

    if colDirection == "right" and rowDirection == "down":
        nextTarget[1] = nextTarget[1] + jump
        if nextTarget[1] > 9:
            nextTarget[0] = nextTarget[0] + jump
            nextTarget[1] = 0

    elif colDirection == "left" and rowDirection == "down":
        nextTarget[1] = nextTarget[1] - jump
        if nextTarget[1] > 9:
            nextTarget[0] = nextTarget[0] + jump
            nextTarget[1] = 0

    
    return [0,0]


# Each time the enemy has a turn, they will select a coordinate in the while loop and then that shot is validated as either a miss or hot
def enemy_turn_input():
    currentTarget = None
    targetRow = None
    targetCol = None
    enemyFindingTarget = True
    enemyMode = ['random'] # random, grid, or kill are the acceptable choices

    # generate a random coordinate and check that it hasn't been fired at before
    # if it has, repeat the loop and generate a new one
    # if it hasn't, exit the loop by setting the enemyFindingTarget flag to false
    while enemyFindingTarget:

        #random search
        currentTarget = generate_random_target()
        targetRow = currentTarget[0]
        targetCol = currentTarget[1]
        if currentTarget not in enemyTargets:
            enemyTargets.append(currentTarget)
            enemyFindingTarget = False   

        #grid search
        # enemyGridStartPos = [0,-1]
        

        #
        # do stuff here
        # 

        #enemyFindingTarget = False

        #post-hit kill search


    # proceeding with the coordinate previously generated as our firing solution
    #  if no ship is there, mark the corresponding square in the gameBoard as a missed shot
    # if the coordinate is not empty sea, then it must be a hit
    # increment the hitcount and inform the player the AI has struck a ship 
    if gameBoard[targetRow][targetCol] == openSea:
        gameBoard[targetRow][targetCol] = missedShot
        alphaRandMiss = coord_to_alphanumeric(currentTarget)
        global enemyLastTurn
        enemyLastTurn = f"THE ENEMY MISSED! Their shot landed at {alphaRandMiss}!"
        print("")
        print("")
    else:
        gameBoard[targetRow][targetCol] = shipStruck
        alphaRandHit = coord_to_alphanumeric(currentTarget)
        hitCounts[1] = hitCounts[1] + 1
        enemyLastTurn = f"THE ENEMY SCORED A HIT! Your ship was struck at {alphaRandHit}!"
        print("")
        print("")


#
#
#   Automated Ship Placement functions   
#
#
def generate_valid_horizontal_placements(shipSize):
    shipSizeOffset = shipSize -1
    validHorzList = []
    for row in range(10):
        for col in range(10):
            if col+shipSizeOffset < 10:
                begTuple = (row,col)
                endTuple = (row, col+shipSizeOffset)
                validHorzList.append((begTuple, endTuple))
    return validHorzList

def generate_valid_vertical_placements(shipSize):
    shipSizeOffset = shipSize -1
    validVertList = []
    for col in range(10):
        for row in range(10):
            if row+shipSizeOffset < 10:
                begTuple = (row,col)
                endTuple = (row+shipSizeOffset, col)
                validVertList.append((begTuple,endTuple))
    return validVertList


def automatic_ship_placement(board, shipName):
    shipSize = shipsHashMap[shipName][0]
    validHorzPlacements = generate_valid_horizontal_placements(shipSize)
    validVertPlacements = generate_valid_vertical_placements(shipSize)
    totalPossibilities = len(validHorzPlacements) + len (validVertPlacements)
    
    seekingValidPlacement = True
    while seekingValidPlacement:
        randNum = int(random.uniform(0, totalPossibilities-1))
        randPair = None
        
        if randNum < len(validHorzPlacements):
            randPair = validHorzPlacements[randNum]
        else:
            randPair = validVertPlacements[randNum-len(validHorzPlacements)]

        full_coords = generate_full_coords(randPair[0],randPair[1])
        if coords_occupied(board, full_coords) != True:
            place_ship(board, shipName, randPair[0], randPair[1])
            seekingValidPlacement = False
        else:
            #print("At least one of the coordinates is already occupied")
            pass

      

def auto_place_all_ships(board):
    automatic_ship_placement(board, "Carrier")
    automatic_ship_placement(board, "Battleship")
    automatic_ship_placement(board, "Cruiser")
    automatic_ship_placement(board, "Submarine")
    automatic_ship_placement(board, "Destroyer")


def generate_random_target():
    rand1 = random.randint(0,9)
    rand2 = random.randint(0,9)
    return (rand1,rand2)



#
#
#   GAME LOOP BEGINS HERE   
#
#

gameOn = True
inputLoop = True
takingTurns = True
turnCounter = 0

input_spacer_no_board()
print_ascii_logo()
input_spacer_with_board()

while gameOn:
        
    while inputLoop:
        userInput = input("Type yes to begin placing ships, auto to have them placed for you, or exit to quit: ")
        if userInput == "exit":
            gameOn = False
            inputLoop = False
        
        elif userInput == "yes":
            print ("\033[A                                                                                             \033[A")
            input_spacer_no_board()
            print("Ships can only be placed vertically or horizontally.")
            print("You will be asked for a pair of coordinates, beginning and end.")
            print("For horizontal placement, beginning should be the left of the two. For vertical, the upper of the two.")
            input_spacer_no_board()
            
            for i in range(5):
                ship_input_loop(shipNameList[i])
                input_spacer_with_board()

            inputLoop = False

        elif userInput == "auto":
            auto_place_all_ships(gameBoard)
            clear_terminal()
            input_spacer_no_board()
            print("YOUR SHIPS HAVE BEEN AUTOMATICALLY PLACED")
            input_spacer_with_board()
            inputLoop = False

        else:
            print("You must enter 'yes', 'auto', or 'exit'!")
        
    
    auto_place_all_ships(enemyBoard)
    clear_and_print_both_boards()

    # uncomment this and the if else in the below while loop to enable automated player firing for quicker testing
    autoChoose = input("type auto to have your firing solutions automated or anything else to proceed normally: ")
    while takingTurns:
        turnCounter +=1
        if hitCounts[0] == 17 or hitCounts[1] == 17:
            takingTurns = False
            print_stats_box()
            print_both_boards()
        else:
            if autoChoose == "auto":
                player_auto_turn_input()
            else:
                player_manual_turn_input()
            #player_auto_turn_input()
        if hitCounts[0] == 17 or hitCounts[1] == 17:
            takingTurns = False
            print_stats_box()
            print_both_boards()
        else:
            enemy_turn_input()
        if hitCounts[0] == 17 or hitCounts[1] == 17:
            takingTurns = False
            print_stats_box()
            print_both_boards()
        else:
            print_stats_box()
            print_both_boards()

    input_spacer_no_board()
    print_ascii_game_over()
    input_spacer_no_board()
    if hitCounts[0] > hitCounts[1]:
        print("You sunk all of your opponents battleships and won the game.")
        print("")
    else:
        print("The enemy sunk all of your battleships and won the game.")
        print("")

    playAgain = input("Would you like to play again? Type yes to play another round or anything else to exit: ")
    if playAgain != 'yes':
        gameOn = False
    else:
        inputLoop = True
        takingTurns = True
        turnCounter = 0
        hitCounts = [0,0]
        clear_terminal()
        for x in range(10):
            for y in range(10):
                gameBoard[x][y] = openSea
                enemyBoard[x][y] = openSea
                targetBoard[x][y] = openSea
        userTargets = []
        enemyTargets = []
        input_spacer_no_board()
        print_ascii_logo()
        input_spacer_with_board()



    #### GAME LOOP TO DO LIST
    #### Next up is tracking of ships sunk/remaining, for game end logic (rather than currently just detecting if a square is a hit or miss and reflecting that)
    #### - consider tracking number of hits AND misses for accuracy stats of player and AI
    #### Once this is complete, can begin implementing levels of AI logic





