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
currentGame = BattleshipInstance()
bs_global_hub.set_game_pointer(currentGame)


print_welcome_screen()

while(gameOn):
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
                ship_input_loop(currentGame.shipNameList[i])
                input_spacer_with_board()

            inputLoop = False

        elif userInput == "auto":
            auto_place_all_ships(currentGame.gameBoard)
            clear_terminal()
            input_spacer_no_board()
            print("YOUR SHIPS HAVE BEEN AUTOMATICALLY PLACED")
            input_spacer_with_board()
            inputLoop = False

        else:
            print("You must enter 'yes', 'auto', or 'exit'!")
        
    
    auto_place_all_ships(currentGame.enemyBoard)
    clear_and_print_both_boards()

    # uncomment this and the if else in the below while loop to enable automated player firing for quicker testing
    autoChoose = input("type auto to have your firing solutions automated or anything else to proceed normally: ")
    while takingTurns:
        currentGame.turnCounter +=1
        hitCounts = currentGame.hitCounts
        if hitCounts[0] == 17 or hitCounts[1] == 17:
            takingTurns = False
            print_stats_box()
            print_both_boards()
        else:
            if autoChoose == "auto":
                player_auto_turn_input()
            else:
                player_manual_turn_input()
            #player_auto_turn_input()
        if hitCounts[0] == 17 or hitCounts[1] == 17:
            takingTurns = False
            print_stats_box()
            print_both_boards()
        else:
            enemy_turn_input()
        if hitCounts[0] == 17 or hitCounts[1] == 17:
            takingTurns = False
            print_stats_box()
            print_both_boards()
        else:
            print_stats_box()
            print_both_boards()

    input_spacer_no_board()
    print_ascii_game_over()
    input_spacer_no_board()
    if hitCounts[0] > hitCounts[1]:
        print("You sunk all of your opponents battleships and won the game.")
        print("")
    else:
        print("The enemy sunk all of your battleships and won the game.")
        print("")

    playAgain = input("Would you like to play again? Type yes to play another round or anything else to exit: ")
    if playAgain != 'yes':
        gameOn = False
    else:
        inputLoop = True
        takingTurns = True
        currentGame.reset_game_instance()
        
        # clear_terminal()
        input_spacer_no_board()
        print_ascii_logo()
        input_spacer_with_board()






