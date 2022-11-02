# import battleship
# import bs_globalvars
from battleship import BattleshipLoop
from bs_globalvars import BattleshipInstance

# main_logic = bs_globalvars.BattleshipInstance()
# main_loop = battleship.BattleshipLoop(main_logic)

main_logic = BattleshipInstance()
main_loop = BattleshipLoop(main_logic)

def get_bs_loop():
    global main_loop
    return main_loop

def get_bs_logic():
    global main_logic
    return main_logic


def main():
    global main_logic
    global main_loop

    # loopInstance = battleship.BattleshipLoop()
    main_loop.welcome_screen()
    gameOn = main_loop.gameOn
 
    while gameOn:
        main_loop.gameLoop()
    

if __name__ == "__main__":
    main()








