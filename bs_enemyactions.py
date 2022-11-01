#
#
#   Enemy AI actions   
#
#
import random
# from battleship import gameBoard
# from battleship import enemyTargets, openSea, missedShot, shipStruck, hitCounts
from bs_globalvars import *
from bs_convhelpers import coord_to_alphanumeric

enemyLastTurn = None

# def setEnemyLastTurn(hitOrMiss, coords):
#     global enemyLastTurn
#     if hitOrMiss == "hit":
#         enemyLastTurn = f"THE ENEMY MISSED! Their shot landed at {coords}!"
#     else:
#         enemyLastTurn = f"THE ENEMY SCORED A HIT! Your ship was struck at {coords}!"



#currentPos is a tuple of 
def traverseGrid(currentPos, leftOrRight, upOrDown, jumpInterval):
    global rdToggle
    nextTarget = currentPos
    colDirection = leftOrRight
    rowDirection = upOrDown
    jump = jumpInterval

    if colDirection == "right" and rowDirection == "down":
        if rdToggle:
            colStartVal = 1
        else:
            colStartVal = 0
        
        nextTarget[1] = nextTarget[1] + jump
        if nextTarget[1] > 9:
            nextTarget[0] = nextTarget[0] + 1
            rdToggle = not rdToggle
            nextTarget[1] = colStartVal

    
    return nextTarget
    #print(nextTarget)
    # if nextTarget == [9,(8 or 9 or 10)]:
    #     flag = False
    
    #return [0,0]


# Each time the enemy has a turn, they will select a coordinate in the while loop and then that shot is validated as either a miss or hot
def enemy_turn_input():
    global enemyLastTurn
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
        # currentTarget = generate_random_target()
        # targetRow = currentTarget[0]
        # targetCol = currentTarget[1]
        # if currentTarget not in enemyTargets:
        #     enemyTargets.append(currentTarget)
        #     enemyFindingTarget = False   

        # grid search
        # 
        global enemyGridPos 
        enemyGridPos = traverseGrid(enemyGridPos,"right","down",2)
        targetRow = enemyGridPos[0]
        targetCol = enemyGridPos[1]
        if enemyGridPos not in enemyTargets:
            enemyGridPos.append(enemyGridPos)
            enemyFindingTarget = False   

        #
        # do stuff here
        # 

        #enemyFindingTarget = False

        #post-hit kill search


    # proceeding with the coordinate previously generated as our firing solution
    #  if no ship is there, mark the corresponding square in the gameBoard as a missed shot
    # if the coordinate is not empty sea, then it must be a hit
    # increment the hitcount and inform the player the AI has struck a ship
    
    #print(targetRow,targetCol)
    if targetRow == 10: # TEMP CODE
        global rdToggle
        rdToggle = not rdToggle
        enemyGridPos = [0,0]
        targetRow = enemyGridPos[0]
        targetCol = enemyGridPos[1]
    #print(targetRow,targetCol)

    if gameBoard[targetRow][targetCol] == openSea:
        gameBoard[targetRow][targetCol] = missedShot
        #alphaRandMiss = coord_to_alphanumeric(currentTarget)
        alphaRandMiss = coord_to_alphanumeric(enemyGridPos)
        enemyLastTurn = f"THE ENEMY MISSED! Their shot landed at {alphaRandMiss}!"
        print("")
        print("")
    else:
        gameBoard[targetRow][targetCol] = shipStruck
        #alphaRandHit = coord_to_alphanumeric(currentTarget)
        alphaRandHit = coord_to_alphanumeric(enemyGridPos)
        hitCounts[1] = hitCounts[1] + 1
        enemyLastTurn = f"THE ENEMY SCORED A HIT! Your ship was struck at {alphaRandHit}!"
        print("")
        print("")







