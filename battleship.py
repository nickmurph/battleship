import random
import os


# TO DO LIST
#
# Adopt more visually appealing grid print method from testhelpers.py
## - settle on symbols for hits, misses, ocean, etc
## - implement colored symbols with colorama?
#
# Also adopt the three tiered approach to the gameboards from testhelpers.py
#
# refactor relevant methods to take in a gameboard as an argument so all methods can be invoked on either players board
#
# next step in game loop will be player/AI taking turns (further details on this and next 3 points at bottom of game loop)
#
# which necessitates an interface for the player choosing their next shot
#
# logic for registering hits and sinkings, ending game
#
# initial AI, which will be blindly/randomly guessing shots
#
# develop further AI models as outlined in notes
#
# AI levels: Hapless Seaman, Admiral Nelson, Fleet Admiral Nimitz
# # Hapless Seaman: This man would be out of his depth commanding a tugboat. 
# # Happy will give random fire orders while cowering beneath deck.
# #
# # Admiral Nelson: Nelson's victory over the French was legendary, but he commanded vessels far less advanced than those present today. 
# # Nelson will intelligently consider firing solutions based on previous hits and misses.
# #
# # Fleet Admiral Nimitz: The greatest admiral of WW2, and the last to hold the title of Fleet Admiral. 
# # Nimitz will offer you the toughest challenge of all (more advanced logic re: traversing the grid, future implementation of remembering player tendencies?)
#
#
# consider refactoring hardcoded 10x10 grid and corresponding logic (eg, checking if, for grid coordinate x, 0 >= x <= 9) into a gridSize variable
# this will allow for arbitrarily scaling the battleship board if a future feature with different grid sizes is implemented
#
#
# player/profile framework of some sort
## - username/password good excuse to demonstrate proper implementation of password hashing/data storage, lays foundation for eventual GUI version
## - having player profiles would also allow for the tracking of tendencies -> future implementation of learning (or at least remembering) AI
#






#
#
# GRID CREATION AND PRINTING, HASHMAP FOR SHIP LENGTHS
#
#
gameBoard = []
enemyBoard = []
openSea = 'O'
shipBody = 'X'
shipStruck = '%'

for x in range(10):
    gameBoard.append([openSea]*10)
    enemyBoard.append([openSea]*10)

def printGameBoard():
    for i in range(10):
        if i == 0:
            print("    1    2    3    4    5    6    7    8    9    1O ")
        curLetter = chr(i+65)
        print(curLetter + " " + str(gameBoard[i]))


# hash map for retrieving size of ships with their name as a key
shipsHashMap = {}
shipsHashMap['Carrier'] = 5
shipsHashMap['Battleship'] = 4
shipsHashMap['Cruiser'] = 3
shipsHashMap['Submarine'] = 3
shipsHashMap['Destroyer'] = 2



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
def square_occupied(grid_tuple):
    return gameBoard[grid_tuple[0]][grid_tuple[1]] == shipBody

def coords_occupied(full_coords):
    flag = False
    for coord in full_coords:
        if square_occupied(coord):
            flag = True
            #print("This coordinate, " + str(coord) + ", is already occupied!")
    return flag



# 
# Places a ship on the grid in the squares between beg and end
# ARGS: string, tuple, tuple
# 
def place_ship(shipName, beg, end):
    shipLength = shipsHashMap[shipName]

    #this is a placement from left to right along a row, with beg as the left coordinates
    if in_same_row(beg,end) and get_col_diff(beg,end) == shipLength-1 and valid_col_bounds(beg,end):
        potential_coords = generate_full_coords(beg,end)
        if coords_occupied(potential_coords) != True:
            for i in range(shipLength):
                gameBoard[beg[0]][beg[1]+i] = shipBody

    #this is a placement from top to bottom along a column, with beg as the top coordinates
    elif in_same_column(beg,end) and get_row_diff(beg,end) == shipLength-1 and valid_row_bounds(beg,end):
        potential_coords = generate_full_coords(beg,end)
        if coords_occupied(potential_coords) != True:
            for i in range(shipLength):
                gameBoard[beg[0]+i][beg[1]] = shipBody
    else:
        raise Exception("These coordinates are invalid!")



#
#
# USER INPUT AND AXIS CONVERSION HELPER FUNCTIONS
#
#

def letter_to_ord(ltr):
    if len(ltr) != 1:
        raise Exception("Letter string larger than 1")
    elif ord(ltr) >= 65 and ord(ltr) <= 75:
        return ord(ltr)
    else:
        raise Exception("Letter outside acceptable ord range")

def ord_to_letter(num):
    if num >= 65 and num <= 75:
        return chr(num)
    else:
        raise Exception("Letter outside acceptable ord range")

def ord_to_grid_num(ordnum):
    return ordnum-65

def validate_user_coord(user_coord):
    row = user_coord[0]
    if len(user_coord) == 2:
        col = int(user_coord[1])
    elif len(user_coord) == 3:
        col = int(user_coord[1] + user_coord[2])
    #print(row,col)

    if len(user_coord) not in range(2,4):
        raise Exception("User coordinate improper length")
    
    elif letter_to_ord(row) != 0 and col in range(1,11):
        row = letter_to_ord(row)
        row = ord_to_grid_num(row)
        col = col -1
        return (row, col)
    else:
        raise Exception("Either row or column input not acceptable")




#
#
# GAME LOOP HELPER FUNCTIONS
#
#

def input_spacer_with_board():
    print("")
    print("")
    printGameBoard()
    print("")
    print("")


def input_spacer_no_board():
    print("")
    print("")    

def clear_terminal():
    os.system('cls||clear')


def print_ascii_logo():
   print( """

                ██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ 
                ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗
                ██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝
                ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ 
                ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     
                ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
                                                                                            
                """)

def ship_input_loop(shipName):
    if shipName == "Carrier":
        print("Your first ship is a " + shipName + ", " + str(shipsHashMap[shipName]) + " squares long.")
    else:
        print("Your next ship is a " + shipName + ", " + str(shipsHashMap[shipName]) + " squares long.")
    
    shipLoop = True
    while shipLoop:
        inputBeg = input("Type the beginning coordinate: ")
        inputEnd = input("Type the ending coordinate: ")
        print("Are your sure you want to start from " + inputBeg + " and end at " + inputEnd +  "?")
        confirmCoords = input("Type yes to continue or no to enter new coordinates: ")
        if confirmCoords == "yes":
            shipBeg = validate_user_coord(inputBeg)
            shipEnd = validate_user_coord(inputEnd)
            place_ship(shipName, shipBeg, shipEnd)
            shipLoop = False
        elif confirmCoords == "no":
            pass
        else:
            print("You must enter 'yes' or 'no'!")





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


def automatic_ship_placement(shipName):
    shipSize = shipsHashMap[shipName]
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
        if coords_occupied(full_coords) != True:
            place_ship(shipName, randPair[0], randPair[1])
            #print("Succesfully placed ship on board")
            seekingValidPlacement = False
        else:
            #print("At least one of the coordinates is already occupied")
            ...

      

def auto_place_all_ships():
    automatic_ship_placement("Carrier")
    automatic_ship_placement("Battleship")
    automatic_ship_placement("Cruiser")
    automatic_ship_placement("Submarine")
    automatic_ship_placement("Destroyer")



#
#
#   GAME LOOP BEGINS HERE   
#
#

gameOn = True

input_spacer_no_board()
# print("Welcome to Battleship!")
print_ascii_logo()
input_spacer_with_board()


inputLoop = True

while gameOn:
        
    while inputLoop:
        userInput = input("Type yes to begin placing ships, auto to have them placed for you, or exit to quit: ")
        if userInput == "exit":
            gameOn = False
            inputLoop = False
        
        elif userInput == "yes":
            print ("\033[A                                                              \033[A")
            input_spacer_no_board()
            print("Ships can only be placed vertically or horizontally.")
            print("You will be asked for a pair of coordinates, beginning and end.")
            print("For horizontal placement, beginning should be the left of the two. For vertical, the upper of the two.")
            input_spacer_no_board()

            ship_input_loop("Carrier")
            input_spacer_with_board()
            ship_input_loop("Battleship")
            input_spacer_with_board()
            ship_input_loop("Cruiser")
            input_spacer_with_board()
            ship_input_loop("Submarine")
            input_spacer_with_board()
            ship_input_loop("Destroyer")
            input_spacer_with_board()

            print("All ships successfully placed!")
            inputLoop = False

        elif userInput == "auto":
            auto_place_all_ships()
            
            clear_terminal()
            input_spacer_no_board()
            print("YOUR SHIPS HAVE BEEN AUTOMATICALLY PLACED")
            input_spacer_with_board()
            inputLoop = False

        else:
            print("You must enter 'yes', 'auto', or 'exit'!")
        break
    #break

print("game loop end")
    #### This is the next stage of the loop, where the AI's board must be populated
    #### populate the enemyBoard using the auto placement function
    #### Then, the user and AI will take turns firing shots
    #### For initial implementation of turns, AI can just be the Hapless Seaman (eg, fires randomly)
    #### - randomly generate a coordinate anywhere from 0,0 to 9,9
    #### - keep track of previous shots and check against that list
    #### - if that coord was fired at already, generate a new one
    #### From there turns should be fairly trivial
    #### - just need user input for shot selectioning using [A-J][1-10] format
    #### Followed by simple checking logic and updating of board with hit and missed squares
    #### Will also need tracking of ships sunk/remaining, for game end logic
    #### - consider tracking number of hits and misses for accuracy stats of player and AI
    #### Once this is complete, 





