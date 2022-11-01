#
#
#   Player action functions   
#
#

# from battleship import gameBoard, enemyBoard, targetBoard
# from battleship import userTargets, openSea, missedShot, shipStruck, hitCounts, shipsHashMap
from bs_globalvars import *
from bs_convhelpers import process_alphanum_to_coord, coord_to_alphanumeric, is_valid_alphanum
from bs_gridhelpers import generate_random_target
from bs_shipplacement import place_ship

userLastTurn = None



def player_manual_turn_input():
    print("It is your turn. Pick a square on the grid to target, of the form [A-J][1-10].")
    print("For Example, to target the uppermost left corner, type A1.")

    global userLastTurn
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

