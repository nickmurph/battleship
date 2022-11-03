#
#
#   Enemy AI actions   
#
#
import copy
from bs_convhelpers import coord_to_alphanumeric
from bs_gridhelpers import *
import bs_global_hub





# returns the nextTarget for grid traversal depending on which direction the grid is being hopped (RD, RU, LD, LU) 
def traverseGrid(currentPos, leftOrRight, upOrDown, jumpInterval):
    game = bs_global_hub.get_game_pointer()
    nextTarget = copy.deepcopy(currentPos)
    jump = jumpInterval

    # RD
    # traversing the board in from top left to bottom right, starting at [0,-1] (enemyGridPos will be auto-set to this at start)
    if leftOrRight == "right" and upOrDown == "down":
        if game.rdToggle:
            colStartVal = 1
        else:
            colStartVal = 0
        
        nextTarget[1] = nextTarget[1] + jump
        if nextTarget[1] > 9:
            nextTarget[0] = nextTarget[0] + 1
            game.rdToggle = not game.rdToggle
            nextTarget[1] = colStartVal


    # RU
    # traversing the board from bottom left to top right starting at [9,-1] (enemyGridPos will be auto-set to this at start)
    if leftOrRight == "right" and upOrDown == "up":
        if game.rdToggle:
            colStartVal = 1
        else:
            colStartVal = 0
        
        nextTarget[1] = nextTarget[1] + jump
        if nextTarget[1] > 9:
            nextTarget[0] = nextTarget[0] - 1
            game.rdToggle = not game.rdToggle
            nextTarget[1] = colStartVal

    # LD
    # traversing the board from top left to bottom right starting at [0,10] (enemyGridPos will be auto-set to this at start)
    if leftOrRight == "left" and upOrDown == "down":
        if game.rdToggle:
            colStartVal = 8
        else:
            colStartVal = 9
        
        nextTarget[1] = nextTarget[1] - jump
        if nextTarget[1] < 0:
            nextTarget[0] = nextTarget[0] + 1
            game.rdToggle = not game.rdToggle
            nextTarget[1] = colStartVal

    # LU
    # traversing the board from bottom left to top right starting at [9,10] (enemyGridPos will be auto-set to this at start)
    if leftOrRight == "left" and upOrDown == "up":
        if game.rdToggle:
            colStartVal = 8
        else:
            colStartVal = 9
        
        nextTarget[1] = nextTarget[1] - jump
        if nextTarget[1] < 0:
            nextTarget[0] = nextTarget[0] - 1
            game.rdToggle = not game.rdToggle
            nextTarget[1] = colStartVal
    
    
    return nextTarget


# Each time the enemy has a turn, they will select a coordinate in the while loop and then that shot is validated as either a miss or hot
def enemy_turn_input(leftOrRight, upOrDown):
    game = bs_global_hub.get_game_pointer()
    currentTarget = None
    targetRow = None
    targetCol = None
    enemyFindingTarget = True

    

    # generate a random coordinate and check that it hasn't been fired at before
    # if it has, repeat the loop and generate a new one
    # if it hasn't, exit the loop by setting the enemyFindingTarget flag to false
    while enemyFindingTarget:

        #random search
        if game.enemyMode == "random":
            currentTarget = generate_random_target()
            targetRow = currentTarget[0]
            targetCol = currentTarget[1]
            if currentTarget not in game.enemyTargets:
                game.enemyTargets.append(currentTarget)
                enemyFindingTarget = False   
            game.enemyGridPos = currentTarget
        
        #grid search
        elif game.enemyMode == "grid":
            currentTarget = traverseGrid(game.enemyGridPos,leftOrRight,upOrDown,2)
            targetRow = currentTarget[0]
            targetCol = currentTarget[1]
            if currentTarget not in game.enemyTargets:
                game.enemyTargets.append(currentTarget)
                enemyFindingTarget = False   
            game.enemyGridPos = currentTarget


        #post-hit kill search        
        elif game.enemyMode == "kill":
             pass
        


 
    # if the AI grid search has traversed the grid from top to bottom or bottom to top, reset it's startingPos and flip the checkerboard pattern
    if game.enemyTraverseLeftOrRight == "right" and game.enemyTraverseUpOrDown == "down" and targetRow == 10:
        game.rdToggle = not game.rdToggle
        game.enemyGridPos = [0,0]
        targetRow = game.enemyGridPos[0]
        targetCol = game.enemyGridPos[1]

    if game.enemyTraverseLeftOrRight == "right" and game.enemyTraverseUpOrDown == "up" and targetRow == -1:
        game.rdToggle = not game.rdToggle
        game.enemyGridPos = [9,0]
        targetRow = game.enemyGridPos[0]
        targetCol = game.enemyGridPos[1]

    if game.enemyTraverseLeftOrRight == "left" and game.enemyTraverseUpOrDown == "down" and targetRow == 10:
        game.rdToggle = not game.rdToggle
        game.enemyGridPos = [0,9]
        targetRow = game.enemyGridPos[0]
        targetCol = game.enemyGridPos[1]

    if game.enemyTraverseLeftOrRight == "left" and game.enemyTraverseUpOrDown == "up" and targetRow == -1:
        game.rdToggle = not game.rdToggle
        game.enemyGridPos = [9,9]
        targetRow = game.enemyGridPos[0]
        targetCol = game.enemyGridPos[1]


    # proceeding with the coordinate previously generated as our firing solution
    # if no ship is there, mark the corresponding square in the playerBoard as a missed shot
    # if the coordinate is not empty sea, then it must be a hit
    # increment the hitcount and inform the player the AI has struck a ship
    #print(targetRow,targetCol)
    if game.playerBoard[targetRow][targetCol] == game.OPEN_SEA:
        game.playerBoard[targetRow][targetCol] = game.MISSED_SHOT
        #alphaRandMiss = coord_to_alphanumeric(currentTarget)
        alphaRandMiss = coord_to_alphanumeric(game.enemyGridPos)
        game.enemyLastTurnMessage = f"THE ENEMY MISSED! Their shot landed at {alphaRandMiss}!"
        print("")
        print("")
    else:
        game.playerBoard[targetRow][targetCol] = game.SHIP_STRUCK
        #alphaRandHit = coord_to_alphanumeric(currentTarget)
        alphaRandHit = coord_to_alphanumeric(game.enemyGridPos)
        game.hitCounts[1] = game.hitCounts[1] + 1
        game.enemyLastTurnMessage = f"THE ENEMY SCORED A HIT! Your ship was struck at {alphaRandHit}!"
        print("")
        print("")







