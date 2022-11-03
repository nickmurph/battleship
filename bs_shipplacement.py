#
#
#   Automated And Manual Ship Placement functions   
#
#

import random
from bs_globalvars import *
from bs_gridhelpers import *
import bs_global_hub



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

# 
# Places a ship on the grid in the squares between beg and end
# ARGS: string, tuple, tuple
# 
def place_ship(board, shipName, beg, end):
    game = bs_global_hub.get_game_pointer()
    shipLength = game.shipsHashMap[shipName][0]
    shipBody = game.shipsHashMap[shipName][1]

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

        
def automatic_ship_placement(board, shipName):
    game = bs_global_hub.get_game_pointer()
    shipSize = game.shipsHashMap[shipName][0]
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
