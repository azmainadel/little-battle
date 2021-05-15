## Global Variables ##
width = 0
height = 0
woods = []
golds = []
foods = []
waters = []
game_map = []

current_player = 1
year = 617

#### IMPORTANT! ####
# Resource array definition: [WOOD, FOOD, GOLD]/[W, F, G]

player_1_resources = [1, 2, 3]
player_2_resources = [1, 2, 3]

spearman_cost = [1, 1, 0]
archer_cost = [1, 0, 1]
knight_cost = [0, 1, 1]
scout_cost = [1, 1, 1]


# Checks for invalid resource positions in
# (0, 1), (1, 0), (2, 1), (1, 2), (width-3, height-2), (width-2, height-3), (width-1, height-2), (width-2, height-1)
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

# Adds resources to the map
def update_map():
    game_map[1][1] = 'H1'
    game_map[width-2][height-2] = 'H2'

    for i in woods:
        game_map[int(i[0])][int(i[1])] = 'WW'
    for i in foods:
        game_map[int(i[0])][int(i[1])] = 'FF'
    for i in golds:
        game_map[int(i[0])][int(i[1])] = 'GG'
    for i in waters:
        game_map[int(i[0])][int(i[1])] = '~~'

# Draws the map
def display_map():
    print('Please check the battlefield, commander.')

    for i in range(width):
        if i==0:
            print("  X0"+str(i), end=" ")
        elif i==width-1:
            print("0"+str(i)+"X")
        else:
            print("0"+str(i), end=" ")

    print(" Y+", end="")
    for i in range(2*width + width-1):
        print("-", end="")
    print("+")

    for i in range(height):
        print("0"+str(i), end="|")

        for j in range(width):
            print(game_map[j][i], end="|")
        print()

    print(" Y+", end="")
    for i in range(2 * width + width -1):
        print("-", end="")
    print("+")

# Prints the prices
def display_prices():
    print("Recruit Prices:\
        \n  Spearman (S) - 1W, 1F\
        \n  Archer (A) - 1W, 1G\
        \n  Knight (K) - 1F, 1G\
        \n  Scout (T) - 1W, 1F, 1G"                                                                                                         )


# Executes the given command
def execute_command(input):
    if input == 'DIS':
        display_map()
    elif input == 'PRIS':
        display_prices()
    else:
        return False

# Check recruitment validity (homebase free/resources free)
def homebase_free():
    if current_player == 1:
        return game_map[1][0] == '  ' or game_map [0][1] == '  ' or game_map [2][1] == '  ' or game_map [1][2] == '  '
    elif current_player == 2:
        # update for you
        return game_map[1][0] == '  ' or game_map [0][1] == '  ' or game_map [2][1] == '  ' or game_map [1][2] == '  '


# Check if input is adjacent to the homebase
def near_homebase(x, y):
    if current_player == 1:
        return (x, y) == (1, 0) or (x, y) == (0, 1) or (x, y) == (2, 1) or (x, y) == (1, 2)
    elif current_player == 2:
        # update for you
        return (x, y) == (1, 0) or (x, y) == (0, 1) or (x, y) == (2, 1) or (x, y) == (1, 2)


# Checks if the army can be recruited
def can_recruit(army):
    if current_player == 1:
        res = player_1_resources
    elif current_player == 2:
        res = player_2_resources

    if army == 'Spearman':
        if spearman_cost[0] > res[0] or spearman_cost[1] > res[1] or spearman_cost[2] > res[2]:
            return False
    elif army == 'Archer':
        if archer_cost[0] > res[0] or archer_cost[1] > res[1] or archer_cost[2] > res[2]:
            return False
    elif army == 'Knight':
        if knight_cost[0] > res[0] or knight_cost[1] > res[1] or knight_cost[2] > res[2]:
            return False
    elif army == 'Scout':
        if scout_cost[0] > res[0] or scout_cost[1] > res[1] or scout_cost[2] > res[2]:
            return False

    return True

# Decrease resources of players based on recruitmen
def decrease_resources(army):
    if current_player == 1:
        if army == 'Spearman':
            player_1_resources[0] -= spearman_cost[0]
            player_1_resources[1] -= spearman_cost[1]
            player_1_resources[2] -= spearman_cost[2]
        if army == 'Archer':
            player_1_resources[0] -= archer_cost[0]
            player_1_resources[1] -= archer_cost[1]
            player_1_resources[2] -= archer_cost[2]
        if army == 'Knight':
            player_1_resources[0] -= knight_cost[0]
            player_1_resources[1] -= knight_cost[1]
            player_1_resources[2] -= knight_cost[2]
        if army == 'Scout':
            player_1_resources[0] -= scout_cost[0]
            player_1_resources[1] -= scout_cost[1]
            player_1_resources[2] -= scout_cost[2]
    elif current_player == 2:
        if army == 'Spearman':
            player_2_resources[0] -= spearman_cost[0]
            player_2_resources[1] -= spearman_cost[1]
            player_2_resources[2] -= spearman_cost[2]
        if army == 'Archer':
            player_2_resources[0] -= archer_cost[0]
            player_2_resources[1] -= archer_cost[1]
            player_2_resources[2] -= archer_cost[2]
        if army == 'Knight':
            player_2_resources[0] -= knight_cost[0]
            player_2_resources[1] -= knight_cost[1]
            player_2_resources[2] -= knight_cost[2]
        if army == 'Scout':
            player_2_resources[0] -= scout_cost[0]
            player_2_resources[1] -= scout_cost[1]
            player_2_resources[2] -= scout_cost[2]


# Validates army recruitment
def handle_recruitment(user_input):
    if user_input == 'S':
        army = 'Spearman'
    elif user_input == 'A':
        army = 'Archer'
    elif user_input == 'K':
        army = 'Knight'
    elif user_input == 'T':
        army = 'Scout'

    if can_recruit(army) == False:
        print("Insufficient resources. Please try again.")
        return
    else:
        while True:
            army_position = input("\nYou want to recruit a " + army +". Enter two integers as format ‘x y’ to place your army.\n")

            if execute_command(user_input) == False:
                army_position = army_position.split()

                if len(army_position) != 2:
                    print("Sorry, invalid input. Try again.")
                else:
                    x = army_position[0]
                    y = army_position[1]

                    if type(int(x)) != int or type(int(y)) != int:
                        print("Sorry, invalid input. Try again.")
                    else:
                        if near_homebase(int(x), int(y)) and game_map[int(x)][int(y)] == '  ':
                            decrease_resources(army)

                            game_map[int(x)][int(y)] = user_input + str(current_player) # K1
                            print("You has recruited a " + army)

                            if current_player == 1:
                                res = player_1_resources
                            elif current_player == 2:
                                res = player_2_resources
                                
                            print("\n[Your Asset: Wood - " + str(res[0]) + " Food - " + str(res[1]) + " Gold - " + str(res[2]) + "]")
                            break
                        else:
                            print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")


############ CODING FLOW STARTS #############

file1 = open("config.txt", "r")
lines = file1.readlines()

labels = []
values = []

if len(lines) == 5:
    for i in range (len(lines)):
        labels.append(lines[i].split(":")[0].strip())
        values.append(lines[i].split(":")[1].strip())

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

    current_value = values[i].split()

    for j in range(len(current_value)):
        if type(int(current_value[j])) != int: # Wrong error
            raise(ValueError("Invalid Configuration File: {} contains non integer characters!".format(labels[i])))

    if len(current_value) % 2 != 0:
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
                            woods.append((current_value[k], current_value[k + 1]))
                        elif labels[i] == 'Food':
                            foods.append((current_value[k], current_value[k + 1]))
                        elif labels[i] == 'Gold':
                            golds.append((current_value[k], current_value[k + 1]))
                        elif labels[i] == 'Water':
                            waters.append((current_value[k], current_value[k + 1]))


# Create map array
game_map = [['  ' for i in range(width)] for j in range(height)]
update_map()
print("Configuration file <filepath> was loaded")

## Config loading complete ##


## Game started ##
print("Game Started: Little Battle! (enter QUIT to quit the game)\n")

display_map()
print("(enter DIS to display the map)\n")
display_prices()
print("(enter PRIS to display the price list)\n")

print("-Year " + str(year) + "-")
print("\n+++Player " + str(current_player) + "'s Stage: Recruit Armies+++")

if current_player == 1:
    res = player_1_resources
elif current_player == 2:
    res = player_2_resources
print("\n[Your Asset: Wood - " + str(res[0]) + " Food - "+ str(res[1]) + " Gold - " + str(res[2]) + "]")

## Recruit army stage ##
while True:
    if res.count(0) >= 2:
        print("No resources to recruit any armies.")
        break

    if homebase_free() == False:
        print("No place to recruit new armies.")
        break

    user_input = input("\nWhich type of army to recruit, (enter) ‘S’, ‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage.\n")

    if execute_command(user_input) == False:
        if user_input == 'NO':
            break
        elif user_input == 'S' or user_input == 'A' or user_input == 'K' or user_input == 'T':
            handle_recruitment(user_input)
        else:
            print("Sorry, invalid input. Try again.")

## Move army stage ##
