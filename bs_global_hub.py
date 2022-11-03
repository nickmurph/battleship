#
# Global variable and getter/setter than can be imported to main and helper files
# allows the establishment and sharing of a global BattleShipInstance object without having to incessantly pass it from main and through a thread of all helper funcs
# cant use a getter in main file and import to helpers, causes cyclical error
global gameLogic

def set_game_pointer(gamePTR):
    global gameLogic
    gameLogic = gamePTR

def get_game_pointer():
    return gameLogic