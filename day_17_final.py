## Global Variables ##
width = 0
height = 0
woods = []
golds = []
foods = []
waters = []
game_map = []


# game_map = [[1, 2], [2, 3]]
# 1 2
# 2 3
# 2d array[row][column]

# Spearman (S) - 1W, 1F
# Archer (A) - 1W, 1G
# Knight (K) - 1F, 1G
# Scout (T) - 1W, 1F, 1G


# (0, 1), (1, 0), (2, 1), (1, 2), (width-3, height-2), (width-2, height-3), (width-1, height-2), (width-2, height-1)
# WIDTH -2 AND MAP HOMEBASE COMPARISON

def invalidPos(x,y):
    if x == 1 and y == 1:
        return False
    elif x == (width-2) and y == (height -2):
        return False
    elif x == 0 and y == 1:
        return False
    elif x == 1 and y == 0:
        return False
    elif x == 2 and y == 1:
        return False
    elif x == 1 and y == 2:
        return False
    elif x == (width -2) and y == (height -3):
        return False
    elif x == width -1 and y == height -2:
        return False
    elif x == width-2 and y == height -1:
        return False
    else:
        return True


# Returns True if input is a duplicate
def isDuplicate(x, y):
    if ((x, y) in woods) or ((x,y) in golds) or ((x, y) in foods) or ((x, y) in waters):
        return True
    return False


###### CODING FLOW STARTS #######

file1 = open("config.txt", "r")
lines = file1.readlines()

labels = []
values = []

if len(lines) == 5:
    for i in range (len(lines)):
        labels.append(lines[i].split(":")[0])
        values.append(lines[i].split(":")[1])

    if labels == ['Frame', 'Water', 'Wood', 'Food', 'Gold']:
           pass
    else:
        raise SyntaxError("Invalid Configuration File: format error!")
else:
    raise SyntaxError("Invalid Configuration File: format error!")


# Validating the frame
dimension_sep = values[0].split("x")

if len(dimension_sep) == 2:
    width = int(dimension_sep[0])
    height = int(dimension_sep[1])

    if width >= 5 and width <= 7 and height >=5 and height <=7:
        pass
    else:      
        raise ArithmeticError("Invalid Configuration File: width and height should range from 5 to 7!")
else:
    raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight!")


# Validating the resources
for i in range(len(values)):
    if i == 0: 
        continue

    current_value = values[i] # eg: '0 2 2 4'

    for j in range(len(current_value)):
        if isinstance(current_value[j], int) == False:   # NOT THE OUTPUT WANTED
            raise(ValueError("Invalid Configuration File: {} contains non integer characters!".format(labels[i])))

    if len(values)% 2 != 0:
        raise SyntaxError("Invalid Configuration File: {} has an odd number of elements!".format(labels[i]))
    else:
        for k in range(0, len(current_value) - 1, 2):
            if (int(current_value[k]) > width or int(current_value[k+1]) > height):
                raise ArithmeticError("Invalid Configuration File: {} contains a position that is out of map.".format(labels[i]))
            else:
                if invalidPos(int(current_value[k]),int(current_value[k+1])) == False:
                    raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied!")
                else:
                    if isDuplicate(current_value[k], current_value[k+1]):
                        raise SyntaxError("Invalid Configuration File: {} has an odd number of elements!".format(labels[i]))
                    else:
                        if labels[i] == 'Wood':
                            woods.append((current_value[k], current_value[k+1]))
                        # do the rest


game_map = [[" "] * width] * height
game_map[1][1] = 'H1'
game_map[width-2][height-2] = 'H2'

for i in woods:
    # i looks like (x, y)
    game_map[i[0]][i[1]] = 'WW'

# Do the rest

print("Configuration file <filepath> was loaded")

## Config loading complete ##


user_input = input("Game Started: Little Battle! (enter QUIT to quit the game)")

if user_input == "QUIT":
    exit()
else:
    print("\nPlease check the battlefield,commander.")

#print the map

map_display = input("(enter DIS to display the map)")

if map_display == "DIS":
    #print the map
    pass
else:
    print("\nRecruit Prices:\
    \n  Spearman (S) - 1W, 1F\
    \n  Archer (A) - 1W, 1G\
    \n  Knight (K) - 1F, 1G\
    \n  Scout (T) - 1W, 1F, 1G")

price_input = input("(enter PRIS to display the price list)")

if price_input == "PRIS":
    #print price list
    pass
else:
    print("\n-Year 617-")
    print("\n+++Player 1's Stage: Recruit Armies+++")
    print("\n[Your Asset: Wood -2 Food- 2 Gold -2]")