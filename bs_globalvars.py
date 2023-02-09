#
#
# CLASS HOLDING ALL OF THE VARIABLES RELATED TO THE GAME BOARD AND ITS STATUS
#
# 

import random
import colorama
from colorama import Fore, Style, init
colorama.init(convert=True)



class BattleshipInstance:
    def __init__(self):
        # constants
        self.OPEN_SEA = Fore.LIGHTCYAN_EX + '__' + Style.RESET_ALL  #formerly used ██, but __ looks cleaner
        self.SHIP_BODY = Fore.GREEN + 'QQ' + Style.RESET_ALL    #currently deprecated but may use in future expansion
        self.SHIP_STRUCK = Fore.RED + 'XX' + Style.RESET_ALL
        self.MISSED_SHOT = Fore.LIGHTCYAN_EX + '00' + Style.RESET_ALL
        
        # board variables
        self.playerBoard = []
        self.enemyBoard = []
        self.targetBoard = []
        self.userTargets = []
        self.enemyTargets = []
        self.hitCounts = [0,0]
        self.turnCounter = 0
        self.userLastTurnMessage = None
        self.enemyLastTurnMessage = None

        # AI targeting variables
        self.enemyGridPos = [0,-1]
        self.enemyMode = "grid" # random, grid, or kill are the valid choices
        self.rdToggle = False
        self.enemyTraverseLeftOrRight = "right" # "left" or "right" are valid choices
        self.enemyTraverseUpOrDown = "down" # "up" or "down" are valid choices

        # ship variables
        self.shipsHashMap = {}
        self.shipNameList = []

        # func calls 
        self.build_ship_lists() 
        self.build_initial_boards()
        self.randomizeEnemyTraversalDirections()
        self.overwriteDefaultsForEnemyTargeting() 



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
        self.randomizeEnemyTraversalDirections()
        self.overwriteDefaultsForEnemyTargeting() 

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

    def overwriteDefaultsForEnemyTargeting(self):
        if self.enemyTraverseLeftOrRight == "right":
            if self.enemyTraverseUpOrDown == "down":
                self.enemyGridPos = [0,-1] # RD
            else:
                self.enemyGridPos = [9,-1] # RU
        elif self.enemyTraverseLeftOrRight == "left":
            if self.enemyTraverseUpOrDown == "down":
                self.enemyGridPos = [0,10] # LD
            else:
                self.enemyGridPos = [9,10] # LU

    def randomizeEnemyTraversalDirections(self):
        # 4 total options: RD, RU, LD, LU
        # let R = 1, L = 0. D = 1, U = 0
        # can view each combination as a 2-bit binary number

        randBin = ""
        for i in range(2):
            curRand = random.randint(0,1)
            randBin = randBin + str(curRand)

        if randBin[0] == '1':
            self.enemyTraverseLeftOrRight = "right"
        elif randBin[0] == '0':
            self.enemyTraverseLeftOrRight = "left"   
        
        if randBin[1] == '1':
                self.enemyTraverseUpOrDown = "down"
        elif randBin[1] == '0':
                self.enemyTraverseUpOrDown = "up"
