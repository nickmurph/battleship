#
#
# CLASS HOLDING ALL OF THE VARIABLES RELATED TO THE GAME BOARD AND ITS STATUS
#
# ██


import colorama
from colorama import Fore, Style, init
colorama.init(convert=True)



class BattleshipInstance:
    def __init__(self):
        # constants
        self.OPEN_SEA = Fore.LIGHTCYAN_EX + '__' + Style.RESET_ALL
        #self.SHIP_BODY = Fore.GREEN + 'QQ' + Style.RESET_ALL
        self.SHIP_STRUCK = Fore.RED + 'XX' + Style.RESET_ALL
        self.MISSED_SHOT = Fore.LIGHTCYAN_EX + '00' + Style.RESET_ALL
        # variables
        self.playerBoard = []
        self.enemyBoard = []
        self.targetBoard = []
        self.userTargets = []
        self.enemyTargets = []
        self.hitCounts = [0,0]
        self.enemyGridPos = [0,-1]
        self.enemyMode = "grid" # random, grid, or kill are the valid choices
        self.rdToggle = False
        self.turnCounter = 0
        self.userLastTurnMessage = None
        self.enemyLastTurnMessage = None
        self.shipsHashMap = {}
        self.shipNameList = []
        self.build_ship_lists() 
        self.build_initial_boards()

    def build_ship_lists(self):
        self.shipsHashMap['Carrier'] = 5, Fore.GREEN + 'AC' + Style.RESET_ALL
        self.shipsHashMap['Battleship'] = 4, Fore.GREEN + 'BS' + Style.RESET_ALL
        self.shipsHashMap['Cruiser'] = 3, Fore.GREEN + 'CR' + Style.RESET_ALL
        self.shipsHashMap['Submarine'] = 3, Fore.GREEN + 'SB' + Style.RESET_ALL
        self.shipsHashMap['Destroyer'] = 2, Fore.GREEN + 'DT' + Style.RESET_ALL
        self.shipNameList = list(self.shipsHashMap.keys())


    def reset_game_instance(self):
        self.turnCounter = 0
        self.hitCounts = [0,0]
        self.userTargets = []
        self.enemyTargets = []
        self.enemyGridPos = [0,-1]
        self.rdToggle = False
        self.playerLastTurnMessage = None
        self.enemyLastTurnMessage = None
        self.reset_boards()

    def build_initial_boards(self):
        for x in range(10):
            self.playerBoard.append([self.OPEN_SEA]*10)
            self.enemyBoard.append([self.OPEN_SEA]*10)
            self.targetBoard.append([self.OPEN_SEA]*10)

    def reset_boards(self):
        for x in range(10):
            for y in range(10):
                self.playerBoard[x][y] = self.OPEN_SEA
                self.enemyBoard[x][y] = self.OPEN_SEA
                self.targetBoard[x][y] = self.OPEN_SEA

    def eitherPlayerHas17Hits(self):
        return (self.hitCounts[0] == 17 or self.hitCounts[1] == 17)

