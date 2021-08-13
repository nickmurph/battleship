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


# consider refactoring hardcoded 10x10 grid and corresponding logic (eg, checking if, for grid coordinate x, 0 >= x <= 9) into a grid size variable
# this will allow for arbitrarily scaling the battleship board if a future feature offering different grid sizes (5x5, 20x20, etc) is implemented

# ROWS, then COLS. So Row 4, Col 5 is gameBoard[4][5]. 
# 0,0 top left and 9,9 bottom right

gameBoard = []
for x in range(10):
    gameBoard.append(['O']*10)


def printGameBoard():
    for i in range(10):
        if i == 0:
            print("  '1', '2', '3', '4', '5', '6', '7', '8', '9', '1O'")
        curLetter = chr(i+65)
        print(curLetter + " " + str(gameBoard[i]))


# hash map for retrieving size of ships with their name as a key
shipsHashMap = {}
shipsHashMap['Carrier'] = 5
shipsHashMap['Battleship'] = 4
shipsHashMap['Cruiser'] = 3
shipsHashMap['Submarine'] = 3
shipsHashMap['Destroyer'] = 2





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





# place_ship('Carrier', (0,0), (4,0))
# place_ship('Submarine', (5,7), (5,9))
# place_ship('Destroyer', (4,8), (5,8))

# for i in range(10):
#     print(gameBoard[i])



gameOn = True

while gameOn:
    print("Welcome to Battleship")
    print("This is the gameboard")
    printGameBoard()
    userInput = input("Choose your placements for ships or type exit to quit: ")
    if userInput == "exit":
        gameOn = False


