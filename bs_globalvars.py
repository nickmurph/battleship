#
#
# GRID CREATION AND PRINTING, HASHMAP FOR SHIP LENGTHS
#
# ██


import colorama
from colorama import Fore, Style, init
colorama.init(convert=True)


gameBoard = []
enemyBoard = []
targetBoard = []
openSea = Fore.LIGHTCYAN_EX + '__' + Style.RESET_ALL
shipBody = Fore.GREEN + 'QQ' + Style.RESET_ALL
shipStruck = Fore.RED + 'XX' + Style.RESET_ALL
missedShot = Fore.LIGHTCYAN_EX + '00' + Style.RESET_ALL
userTargets = []
enemyTargets = []
hitCounts = [0,0]
enemyGridPos = [0,-1]
rdToggle = False
turnCounter = 0

# hash map for retrieving size of ships with their name as a key
shipsHashMap = {}
shipsHashMap['Carrier'] = 5, Fore.GREEN + 'AC' + Style.RESET_ALL
shipsHashMap['Battleship'] = 4, Fore.GREEN + 'BS' + Style.RESET_ALL
shipsHashMap['Cruiser'] = 3, Fore.GREEN + 'CR' + Style.RESET_ALL
shipsHashMap['Submarine'] = 3, Fore.GREEN + 'SB' + Style.RESET_ALL
shipsHashMap['Destroyer'] = 2, Fore.GREEN + 'DT' + Style.RESET_ALL

shipNameList = list(shipsHashMap.keys())