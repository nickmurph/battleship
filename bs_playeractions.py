#
#
#   Player action functions   
#
#

from webbrowser import get
from bs_globalvars import *
from bs_convhelpers import process_alphanum_to_coord, coord_to_alphanumeric, is_valid_alphanum
from bs_gridhelpers import generate_random_target
from bs_shipplacement import place_ship
import bs_global_hub

def player_manual_turn_input():
    game = bs_global_hub.get_game_pointer()
    global userLastTurn
    gridTarget = None
    rowTarget = None
    colTarget = None
    userFindingTarget = True

    print("It is your turn. Pick a square on the grid to target, of the form [A-J][1-10].")
    print("For Example, to target the uppermost left corner, type A1.")

    while userFindingTarget:
        inputTarget = input("Type the coordinate you want to target: ")
        gridTarget = process_alphanum_to_coord(inputTarget)
        if gridTarget == False:
            print("The given input was not a valid coordinate.")
            continue
        rowTarget = gridTarget[0]
        colTarget = gridTarget[1]

        if gridTarget in game.userTargets:
            print("You have already entered this target, choose another.")
        else:
            game.userTargets.append(gridTarget)
            if game.enemyBoard[rowTarget][colTarget] == game.openSea:
                game.targetBoard[rowTarget][colTarget] = game.missedShot
                print("")
                userLastTurn = f"YOU MISSED! No enemy ship at {inputTarget}!"
            else:
                game.targetBoard[rowTarget][colTarget] = game.shipStruck
                game.hitCounts[0] = game.hitCounts[0] + 1
                print("")
                userLastTurn = f"YOU SCORED A HIT! Enemy ship struck at {inputTarget}!"
            userFindingTarget = False



def player_auto_turn_input():
    game = bs_global_hub.get_game_pointer()
    randomTarget = None
    randRow = None
    randCol = None
    userAutoFindingTarget = True
    while userAutoFindingTarget:
        randomTarget = generate_random_target()
        randRow = randomTarget[0]
        randCol = randomTarget[1]
        if randomTarget not in game.userTargets:
            game.userTargets.append(randomTarget)
            userAutoFindingTarget = False
    if game.enemyBoard[randRow][randCol] == game.openSea:
        game.targetBoard[randRow][randCol] = game.missedShot
        alphaRandMiss = coord_to_alphanumeric(randomTarget)
        global userLastTurn
        userLastTurn = f"YOU MISSED! No enemy ship at {alphaRandMiss}!"
        print("")
        print("")
    else:
        game.targetBoard[randRow][randCol] = game.shipStruck
        alphaRandHit = coord_to_alphanumeric(randomTarget)
        game.hitCounts[0] = game.hitCounts[0] + 1
        userLastTurn = f"YOU SCORED A HIT! Enemy ship struck at {alphaRandHit}!"
        print("")
        print("")



def ship_input_loop(shipName):
    game = bs_global_hub.get_game_pointer()
    shipsHashMap = game.shipsHashMap

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

        if place_ship(game.gameBoard, shipName, inputBeg, inputEnd) != False:
            shipLoop = False
        else:
            print("The coordinates you chose were sized improperly or occupied!")
            print(f"try again with coordinates {shipsHashMap[shipName][0]} spaces apart, vertically or horizontally.")

