def testhelperfunc(num):
    print("blerp" + str(num))



gameBoard = []
for x in range(10):
    gameBoard.append(['O']*10)


for x in range(0,5):
    gameBoard[x][0] = 'X'
    print(x,0)



def printGameBoard():
    for i in range(10):
        if i == 0:
            print("    1    2    3    4    5    6    7    8    9    1O ")
        curLetter = chr(i+65)
        print(curLetter + " " + str(gameBoard[i]))


printGameBoard()




# For AI placement
# Give player option to randomize as well?
# generate pairs of tuples (beg, end)
# Randomly select one of those pairs for first ship and add it to the board
# Randomly select next pair, checking that theres no overlap
# worth considering paradigms for tracking covered squares and comparing
        # check if beg and end empty first
        # if so use generate full funct and check those? O(1) to check any coordinate, and generate full is at most O(5)
        # hash map might better if board was theoretically infinite but these are hard limits for now
        # if the board is made dynamically resizable in future iteration and larger ships added there still won't be any lengths over 10 so "O(n)" means far less here

def generate_valid_horizontal_placements(shipSize):
    shipSizeOffset = shipSize -1
    for row in range(10):
        for col in range(10):
            if col+shipSizeOffset < 10:
                print(str(row) + "," + str(col) + ",  " + str(row) +","+ str(col+shipSizeOffset))
        print("")

def generate_valid_vertical_placements(shipSize):
    shipSizeOffset = shipSize -1
    for col in range(10):
        for row in range(10):
            if row+shipSizeOffset < 10:
                print(str(row) + "," + str(col) + ",  " + str(row+shipSizeOffset) +","+ str(col))
        print("")


#generate_valid_horizontal_placements(5)
#generate_valid_vertical_placements(5)


print("█")


print(str(gameBoard[0]))
print(' '.join(gameBoard[0]))