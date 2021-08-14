import random



#TO DO LIST
#
# Game loop that takes in and saves user input or allows them to exit main loop
#
# function to convert user input for ship placement and call place_ship
#
# create second gameboard now that grid concept is fleshed out
# refactor relevant methods to take in a gameboard as an argument so all methods can be invoked on either players board
#
# player/profile framework of some sort 
#
# interface for choosing ship placements
#
# an initial game loop wherein players take turns
#
# logic for registering hits and sinkings, ending game
#
# initial AI, which will be blindly/randomly guessing shots
#
# develop further AI models as outlined in notes
#
# AI levels: Hapless Seaman, Admiral Nelson, Fleet Admiral Nimitz
#
# # Hapless Seaman: This man would be out of his depth commanding a tugboat. 
# # Happy will give random fire orders while cowering beneath deck.
# #
# # Admiral Nelson: Hero of Trafalgar; Nelson's victory over the French was legendary, but he commanded vessels far less advanced than those present today. 
# # Nelson will intelligently consider firing solutions based on previous hits and misses.
# #
# # Fleet Admiral Nimitz: The greatest admiral of WW2, and the last to hold the title of Fleet Admiral. 
# # Nimitz will offer you the toughest challenge of all.


# consider refactoring hardcoded 10x10 grid and corresponding logic (eg, checking if, for grid coordinate x, 0 >= x <= 9) into a grid size variable
# this will allow for arbitrarily scaling the battleship board if a future feature offering different grid sizes (5x5, 20x20, etc) is implemented

# ROWS, then COLS. So Row 4, Col 5 is gameBoard[4][5]. 
# 0,0 top left and 9,9 bottom right






#
#
# GRID CREATION AND PRINTING, HASHMAP FOR SHIP LENGTHS
#
#
gameBoard = []
for x in range(10):
    gameBoard.append(['O']*10)

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
    return gameBoard[grid_tuple[0]][grid_tuple[1]] == 'X'

def coords_occupied(full_coords):
    flag = False
    for coord in full_coords:
        if square_occupied(coord):
            flag = True
            print("This coordinate, " + str(coord) + ", is already occupied!")
    return flag



# This may be over-engineered in comparison to old placing function(s)
# is abstracting out messy math with helper functions more readable?
# Or does it result in a pause to understand what each function might be doing, whereas the bare math was more obvious despite the mess?
def place_ship(shipName, beg, end):
    shipLength = shipsHashMap[shipName]

    #this is a placement from left to right along a row, with beg as the left coordinates
    if in_same_row(beg,end) and get_col_diff(beg,end) == shipLength-1 and valid_col_bounds(beg,end):
        potential_coords = generate_full_coords(beg,end)
        if coords_occupied(potential_coords) != True:
            for i in range(shipLength):
                gameBoard[beg[0]][beg[1]+i] = 'X'

    #this is a placement from top to bottom along a column, with beg as the top coordinates
    elif in_same_column(beg,end) and get_row_diff(beg,end) == shipLength-1 and valid_row_bounds(beg,end):
        potential_coords = generate_full_coords(beg,end)
        if coords_occupied(potential_coords) != True:
            for i in range(shipLength):
                gameBoard[beg[0]+i][beg[1]] = 'X'
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
    print(row,col)

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

def print_board_input_spacer():
    print("")
    print("")
    printGameBoard()
    print("")
    print("")


#
#
#   GAME LOOP BEGINS HERE   
#
#

gameOn = True

print("")
print("Welcome to Battleship!")
print_board_input_spacer()
while gameOn:
    userInput = input("Type yes to begin placing ships or exit to quit: ")
    inputLoop = True
    while inputLoop:
        if userInput == "exit":
            gameOn = False
            inputLoop = False
        elif userInput == "yes":
            print("")
            print("Your first ship is an Aircraft Carrier, 5 squares long.")
            print("Ships can only be placed vertically or horizontally.")
            print("You will be asked for a pair of coordinates, beginning and end.")
            print("For horizontal placement, beginning should be the left of the two. For vertical, the upper of the two.")
            print("Example valid input for the Aircraft Carrier:")
            print("-Beginning: A1, End: A5")
            carrierLoop = True
            while carrierLoop:
                inputBeg = input("Type the beginning coordinate: ")
                inputEnd = input("Type the ending coordinate: ")
                print("Are your sure you want to start from " + inputBeg + " and end at " + inputEnd +  "?")
                confirmCoords = input("Type yes to continue or no to enter new coordinates: ")
                if confirmCoords == "yes":
                    battleshipBeg = validate_user_coord(inputBeg)
                    battleshipEnd = validate_user_coord(inputEnd)
                    print(battleshipBeg)
                    print(battleshipEnd)
                    place_ship("Carrier", battleshipBeg, battleshipEnd)
                    carrierLoop = False
                elif confirmCoords == "no":
                    pass
                else:
                    print("You must enter 'yes' or 'no'!")


            print_board_input_spacer()
            print("Your next ship is a Battleship, 4 squares long.")
            battleshipLoop = True
            while battleshipLoop:
                inputBeg = input("Type the beginning coordinate: ")
                inputEnd = input("Type the ending coordinate: ")
                print("Are your sure you want to start from " + inputBeg + " and end at " + inputEnd +  "?")
                confirmCoords = input("Type yes to continue or no to enter new coordinates: ")
                if confirmCoords == "yes":
                    battleshipBeg = validate_user_coord(inputBeg)
                    battleshipEnd = validate_user_coord(inputEnd)
                    print(battleshipBeg)
                    print(battleshipEnd)
                    place_ship("Battleship", battleshipBeg, battleshipEnd)
                    battleshipLoop = False
                elif confirmCoords == "no":
                    pass
                else:
                    print("You must enter 'yes' or 'no'!")


            print_board_input_spacer()
            print("Your next ship is a Cruiser, 3 squares long.")
            cruiserLoop = True
            while cruiserLoop:
                inputBeg = input("Type the beginning coordinate: ")
                inputEnd = input("Type the ending coordinate: ")
                print("Are your sure you want to start from " + inputBeg + " and end at " + inputEnd +  "?")
                confirmCoords = input("Type yes to continue or no to enter new coordinates: ")
                if confirmCoords == "yes":
                    cruiserBeg = validate_user_coord(inputBeg)
                    cruiserEnd = validate_user_coord(inputEnd)
                    print(cruiserBeg)
                    print(cruiserEnd)
                    place_ship("Cruiser", cruiserBeg, cruiserEnd)
                    cruiserLoop = False
                elif confirmCoords == "no":
                    pass
                else:
                    print("You must enter 'yes' or 'no'!")


            print_board_input_spacer()
            print("Your next ship is a Submarine, 3 squares long.")
            submarineLoop = True
            while submarineLoop:
                inputBeg = input("Type the beginning coordinate: ")
                inputEnd = input("Type the ending coordinate: ")
                print("Are your sure you want to start from " + inputBeg + " and end at " + inputEnd +  "?")
                confirmCoords = input("Type yes to continue or no to enter new coordinates: ")
                if confirmCoords == "yes":
                    submarineBeg = validate_user_coord(inputBeg)
                    submarineEnd = validate_user_coord(inputEnd)
                    print(submarineBeg)
                    print(submarineEnd)
                    place_ship("Submarine", submarineBeg, submarineEnd)
                    submarineLoop = False
                elif confirmCoords == "no":
                    pass
                else:
                    print("You must enter 'yes' or 'no'!")


            print_board_input_spacer()
            print("Your next ship is a Destroyer, 2 squares long.")
            destroyerLoop = True
            while destroyerLoop:
                inputBeg = input("Type the beginning coordinate: ")
                inputEnd = input("Type the ending coordinate: ")
                print("Are your sure you want to start from " + inputBeg + " and end at " + inputEnd +  "?")
                confirmCoords = input("Type yes to continue or no to enter new coordinates: ")
                if confirmCoords == "yes":
                    destroyerBeg = validate_user_coord(inputBeg)
                    destroyerEnd = validate_user_coord(inputEnd)
                    print(destroyerBeg)
                    print(destroyerEnd)
                    place_ship("Destroyer", destroyerBeg, destroyerEnd)
                    destroyerLoop = False
                elif confirmCoords == "no":
                    pass
                else:
                    print("You must enter 'yes' or 'no'!")

            
            print_board_input_spacer()
            print("All ships successfully placed!")
            inputLoop = False
            


        else:
            print("You must enter 'yes' or 'exit'!")
            break

