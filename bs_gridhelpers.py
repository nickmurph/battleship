#
#
# GRID RELATED HELPER FUNCTIONS
#
#

import random
# from battleship import openSea
from bs_globalvars import *

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


def generate_random_target():
    rand1 = random.randint(0,9)
    rand2 = random.randint(0,9)
    return (rand1,rand2)