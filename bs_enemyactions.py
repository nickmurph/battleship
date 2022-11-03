#
#
#   Enemy AI actions   
#
#
import copy
from bs_convhelpers import coord_to_alphanumeric
from bs_gridhelpers import *
import bs_global_hub

enemyLastTurn = None


#currentPos is a tuple of 
def traverseGrid(currentPos, leftOrRight, upOrDown, jumpInterval):
    game = bs_global_hub.get_game_pointer()
    nextTarget = copy.deepcopy(currentPos)
    colDirection = leftOrRight
    rowDirection = upOrDown
    jump = jumpInterval

    if colDirection == "right" and rowDirection == "down":
        if game.rdToggle:
            colStartVal = 1
        else:
            colStartVal = 0
        
        nextTarget[1] = nextTarget[1] + jump
        if nextTarget[1] > 9:
            nextTarget[0] = nextTarget[0] + 1
            game.rdToggle = not game.rdToggle
            nextTarget[1] = colStartVal
            # print(rdToggle)
    
    #print(currentPos, nextTarget)
    return nextTarget


# Each time the enemy has a turn, they will select a coordinate in the while loop and then that shot is validated as either a miss or hot
def enemy_turn_input():
    game = bs_global_hub.get_game_pointer()
    global enemyLastTurn
    currentTarget = None
    targetRow = None
    targetCol = None
    enemyFindingTarget = True

    

    # generate a random coordinate and check that it hasn't been fired at before
    # if it has, repeat the loop and generate a new one
    # if it hasn't, exit the loop by setting the enemyFindingTarget flag to false
    while enemyFindingTarget:

        if game.enemyMode == "random":
            #random search
            currentTarget = generate_random_target()
            targetRow = currentTarget[0]
            targetCol = currentTarget[1]
            if currentTarget not in game.enemyTargets:
                game.enemyTargets.append(currentTarget)
                enemyFindingTarget = False   
            game.enemyGridPos = currentTarget
            print(game.enemyTargets)

        elif game.enemyMode == "grid":
            # grid search
            currentTarget = traverseGrid(game.enemyGridPos,"right","down",2)
            targetRow = currentTarget[0]
            targetCol = currentTarget[1]
            if currentTarget not in game.enemyTargets:
                game.enemyTargets.append(currentTarget)
                enemyFindingTarget = False   
            game.enemyGridPos = currentTarget
            #print(game.enemyTargets)
        
        elif game.enemyMode == "kill":
            #post-hit kill search
             pass
        


    # proceeding with the coordinate previously generated as our firing solution
    #  if no ship is there, mark the corresponding square in the gameBoard as a missed shot
    # if the coordinate is not empty sea, then it must be a hit
    # increment the hitcount and inform the player the AI has struck a ship
    
    print(targetRow,targetCol)
    if targetRow == 10: # TEMP CODE
        game.rdToggle = not game.rdToggle
        game.enemyGridPos = [0,0]
        targetRow = game.enemyGridPos[0]
        targetCol = game.enemyGridPos[1]
    #print(targetRow,targetCol)

    if game.gameBoard[targetRow][targetCol] == game.openSea:
        game.gameBoard[targetRow][targetCol] = game.missedShot
        #alphaRandMiss = coord_to_alphanumeric(currentTarget)
        alphaRandMiss = coord_to_alphanumeric(game.enemyGridPos)
        enemyLastTurn = f"THE ENEMY MISSED! Their shot landed at {alphaRandMiss}!"
        print("")
        print("")
    else:
        game.gameBoard[targetRow][targetCol] = game.shipStruck
        #alphaRandHit = coord_to_alphanumeric(currentTarget)
        alphaRandHit = coord_to_alphanumeric(game.enemyGridPos)
        game.hitCounts[1] = game.hitCounts[1] + 1
        enemyLastTurn = f"THE ENEMY SCORED A HIT! Your ship was struck at {alphaRandHit}!"
        print("")
        print("")







