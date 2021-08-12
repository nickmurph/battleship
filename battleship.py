import random




# consider refactoring hardcoded 10x10 grid and corresponding logic (eg, checking if, for grid coordinate x, 0 >= x <= 9) into a grid size variable
# this will allow for arbitrarily scaling the battleship board if a future feature offering different grid sizes (5x5, 20x20, etc) is implemented

# ROWS, then COLS. So Row 4, Col 5 is gameBoard[4][5]. 
# 0,0 top left and 9,9 bottom right
gameBoard = []
for x in range(10):
    gameBoard.append(['O']*10)



# generate_full_coords(beg, end)
# take in two tuples, begin and end, and return all of the coordinates contained between those two points
# eg, beg = (0,0) and end = (0,9) would return all of the coordinates in row 0
def generate_full_coords(beg, end):
    pass


#returns True if the coordinate sent as an argument already has a ship occupying it on the board
def square_occupied(grid_tuple):
    return gameBoard[grid_tuple[0]][grid_tuple[1]] != 'O'





# obvious next move is to refactor these individual place_X functions into one single place_ship function
# wrote place_carrier first to test grid logic and lazily copy pasted with minor adjustments
# -add another parameter to function call that corresponds to the ship name (or ship size)
# -abstract out the size of the ship from the if checks and replace it with a constant value corresponding to the ship sent as argument
# -example for above, using place_carrier: the "== 4" and the "range(5)") 

def place_carrier(beg, end):
    #this is a placement from left to right along a row, with beg as the left coordinates
    if beg[0] == end[0] and end[1] - beg[1] == 4 and beg[1] >= 0 and end[1] <= 9:
        for i in range(5):
            gameBoard[beg[0]][beg[1]+i] = 'X'

    #this is a placement from top to bottom along a column, with beg as the 'top' coordinates
    if beg[1] == end[1] and end[0] - beg[0] == 4 and beg[0] >= 0 and end[0] <= 9:
        for i in range(5):
            gameBoard[beg[0]+i][beg[1]] = 'X'
    
    else:
        raise Exception("These coordinates are invalid!")


def place_battleship(beg,end):
    if beg[0] == end[0] and end[1] - beg[1] == 3 and beg[1] >= 0 and end[1] <= 9:
        for i in range(4):
            gameBoard[beg[0]][beg[1]+i] = 'X'
    if beg[1] == end[1] and end[0] - beg[0] == 3 and beg[0] >= 0 and end[0] <= 9:
        for i in range(4):
            gameBoard[beg[0]+i][beg[1]] = 'X'

def place_cruiser(beg, end):
    if beg[0] == end[0] and end[1] - beg[1] == 2 and beg[1] >= 0 and end[1] <= 9:
        for i in range(3):
            gameBoard[beg[0]][beg[1]+i] = 'X'
    if beg[1] == end[1] and end[0] - beg[0] == 2 and beg[0] >= 0 and end[0] <= 9:
        for i in range(3):
            gameBoard[beg[0]+i][beg[1]] = 'X'

def place_submarine(beg, end):
    if beg[0] == end[0] and end[1] - beg[1] == 2 and beg[1] >= 0 and end[1] <= 9:
        for i in range(3):
            gameBoard[beg[0]][beg[1]+i] = 'X'
    if beg[1] == end[1] and end[0] - beg[0] == 2 and beg[0] >= 0 and end[0] <= 9:
        for i in range(3):
            gameBoard[beg[0]+i][beg[1]] = 'X'

def place_cruiser(beg, end):
    if beg[0] == end[0] and end[1] - beg[1] == 1 and beg[1] >= 0 and end[1] <= 9:
        for i in range(2):
            gameBoard[beg[0]][beg[1]+i] = 'X'
    if beg[1] == end[1] and end[0] - beg[0] == 1 and beg[0] >= 0 and end[0] <= 9:
        for i in range(2):
            gameBoard[beg[0]+i][beg[1]] = 'X'
    



place_carrier((0,0), (4,0)) 


place_submarine((5,7), (5,9))


for i in range(10):
    print(gameBoard[i])



