#
#
# USER INPUT AND AXIS CONVERSION HELPER FUNCTIONS
#
#

def letter_to_ord(ltr):
    if len(ltr) != 1:
        raise Exception("Letter string larger than 1")
    elif ord(ltr) >= 65 and ord(ltr) < 75:
        return ord(ltr)
    else:
        raise Exception("Letter outside acceptable ord range")

def ord_to_letter(num):
    if num >= 65 and num < 75:
        return chr(num)
    else:
        raise Exception("Letter outside acceptable ord range")

def ord_to_grid_num(ordnum):
    return ordnum-65

def grid_num_to_ord(gridNum):
    return gridNum+65

def is_valid_alphanum(inputStr):
    if type(inputStr) != type(""):
        return False
    elif len(inputStr) not in range(2,4):
        return False
    elif inputStr[0] not in "ABCDEFGHIJ":
        return False
    elif int(inputStr[1]) not in range(1,11):
        return False
    elif len(inputStr) == 3 and int(inputStr[1] + inputStr[2]) not in range (1,11):
        return False
    else:
        return True


def process_alphanum_to_coord(user_coord):
    try:
        row = user_coord[0]
        if len(user_coord) == 2:
            col = int(user_coord[1])
        elif len(user_coord) == 3:
            col = int(user_coord[1] + user_coord[2])

        if len(user_coord) not in range(2,4):
            raise Exception("User coordinate improper length")
        
        elif letter_to_ord(row) != 0 and col in range(1,11):
            row = letter_to_ord(row)
            row = ord_to_grid_num(row)
            col = col -1
            return (row, col)
        else:
            raise Exception("Either row or column input not acceptable")
    except:
        return False

def coord_to_alphanumeric(coord):
    row = coord[0]
    col = coord[1]
    row = grid_num_to_ord(row)
    row = ord_to_letter(row)
    col += 1
    return row + (str(col))
