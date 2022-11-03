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
        self.gameBoard = []
        self.enemyBoard = []
        self.targetBoard = []
        self.openSea = Fore.LIGHTCYAN_EX + '__' + Style.RESET_ALL
        self.shipBody = Fore.GREEN + 'QQ' + Style.RESET_ALL
        self.shipStruck = Fore.RED + 'XX' + Style.RESET_ALL
        self.missedShot = Fore.LIGHTCYAN_EX + '00' + Style.RESET_ALL
        self.userTargets = []
        self.enemyTargets = []
        self.hitCounts = [0,0]
        self.enemyGridPos = [0,-1]
        self.enemyMode = "grid" # random, grid, or kill are the acceptable choices
        self.rdToggle = False
        self.turnCounter = 0
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
        self.reset_boards()

    def build_initial_boards(self):
        for x in range(10):
            self.gameBoard.append([self.openSea]*10)
            self.enemyBoard.append([self.openSea]*10)
            self.targetBoard.append([self.openSea]*10)

    def reset_boards(self):
        for x in range(10):
            for y in range(10):
                self.gameBoard[x][y] = self.openSea
                self.enemyBoard[x][y] = self.openSea
                self.targetBoard[x][y] = self.openSea