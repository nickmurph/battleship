from bs_convhelpers import *
from bs_enemyactions import *
from bs_gridhelpers import *
from bs_playeractions import *
from bs_playeractions import *
from bs_printhelpers import *
from bs_shipplacement import *
from bs_globalvars import *
import bs_global_hub






gameOn = True
inputLoop = True
takingTurns = True
game = BattleshipInstance()
bs_global_hub.set_game_pointer(game)


print_welcome_screen()

while(gameOn):
    # player trapped in this loop which repeats until they have picked their settings and placed their ships
    while inputLoop:
        userInput = input("Type yes to begin placing ships, auto to have them placed for you, or exit to quit: ")
        if userInput == "exit":
            gameOn = False
            inputLoop = False
        
        elif userInput == "yes":
            print ("\033[A                                                                                             \033[A")
            input_spacer_no_board()
            print("Ships can only be placed vertically or horizontally.")
            print("You will be asked for a pair of coordinates, beginning and end.")
            print("For horizontal placement, beginning should be the left of the two. For vertical, the upper of the two.")
            input_spacer_no_board()
            
            for i in range(5):
                ship_input_loop(game.shipNameList[i])
                input_spacer_with_board()

            inputLoop = False

        elif userInput == "auto":
            auto_place_all_ships(game.playerBoard)
            clear_terminal()
            input_spacer_no_board()
            print("YOUR SHIPS HAVE BEEN AUTOMATICALLY PLACED")
            input_spacer_with_board()
            inputLoop = False

        else:
            print("You must enter 'yes', 'auto', or 'exit'!")
        
    
    # place the enemy ships automatically and print the two boards
    auto_place_all_ships(game.enemyBoard)
    clear_and_print_both_boards()


    autoChoose = input("type auto to have your firing solutions automated or anything else to proceed normally: ")
    # player trapped in this loop while player and AI take turns
    while takingTurns:
        game.turnCounter +=1
        print(game.hitCounts)

        # if either player has 17 hits, the game is over
        # if not, it's the players turn 
        if game.eitherPlayerHas17Hits():
            takingTurns = False
            print_stats_and_both_boards()
            continue
        else:
            if autoChoose == "auto":
                player_auto_turn_input()
            else:
                player_manual_turn_input()

        # check again if anybody has 17 hits after the player has just gone
        # if not, it's the enemy's turn  
        if game.eitherPlayerHas17Hits():
            takingTurns = False
            print_stats_and_both_boards()
            continue
        else:
            enemy_turn_input()
        
        # check once more for the winning condition
        # if not, the loop will repeat from the top, continue ad infinitum until a winner reaches 17 hits
        if game.eitherPlayerHas17Hits():
            takingTurns = False
            print_stats_and_both_boards()
            continue
        else:
            print_stats_and_both_boards()


    # if the above loop has escaped, somebody reached 17 hits to win
    # if it was the player, print victory message. If enemy, print defeat message
    if game.hitCounts[0] > game.hitCounts[1]:
        print("You sunk all of your opponents battleships and won the game.")
        print("")
    else:
        print("The enemy sunk all of your battleships and won the game.")
        print("")


    # Ask the player if they'd like to play again, exiting loop if no, resetting game and starting the loop over if yes
    playAgain = input("Would you like to play again? Type yes to play another round or anything else to exit: ")
    if playAgain != 'yes':
        gameOn = False
    else:
        inputLoop = True
        takingTurns = True
        game.reset_game_instance()
        print_welcome_screen()






