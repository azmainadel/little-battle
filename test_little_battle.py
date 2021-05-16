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

class Player:
    def __init__(self, id):
        self.id = id
        self.wood = 2
        self.food = 2
        self.gold = 2
        self.spearmen = []
        self.archers = []
        self.knights = []
        self.scouts = []
        self.current_moves = []

    def recruit(self, army, x, y):
        if army == 'Spearman':
            self.wood -= spearman_cost[0]
            self.food -= spearman_cost[1]
            self.gold -= spearman_cost[2]
            self.spearmen.append((x, y))
        elif army == 'Archer':
            self.wood -= archer_cost[0]
            self.food -= archer_cost[1]
            self.gold -= archer_cost[2]
            self.archers.append((x, y))
        elif army == 'Knight':
            self.wood -= knight_cost[0]
            self.food -= knight_cost[1]
            self.gold -= knight_cost[2]
            self.knights.append((x, y))
        elif army == 'Scout':
            self.wood -= scout_cost[0]
            self.food -= scout_cost[1]
            self.gold -= scout_cost[2]
            self.scouts.append((x, y))

    def has_min_resources(self):
        resources = [self.wood, self.food, self.gold]
        if resources.count(0) >= 2:
            return False
        else:
            return True

    def has_army_to_move(self):
        if len(self.spearmen) > 0 or len(self.archers) > 0 or len(self.knights) > 0 or len(self.scouts) > 0:
            if (len(self.spearmen) + len(self.archers) + len(self.knights) + len(self.scouts)) == len(self.current_moves):
                return False
            else:
                return True
        return False

    def print_armies_to_move(self):
        print("\nArmies to Move:")

        temp = list(set(self.spearmen)-set(self.current_moves))
        if len(temp) > 0:
            print("  Spearman: ", end="")
            print(*temp, sep=", ")

        temp = list(set(self.archers) - set(self.current_moves))
        if len(temp) > 0:
            print("  Archer: ", end="")
            print(*temp, sep=", ")

        temp = list(set(self.knights) - set(self.current_moves))
        if len(temp) > 0:
            print("  Knight: ", end="")
            print(*temp, sep=", ")

        temp = list(set(self.scouts) - set(self.current_moves))
        if len(temp) > 0:
            print("  Scout: ", end="")
            print(*temp, sep=", ")

    def delete_army(self, x, y):
        self.current_moves.remove((x, y))

        if (x, y) in self.spearmen:
            self.spearmen.remove((x, y))
        elif (x, y) in self.archers:
            self.archers.remove((x, y))
        elif (x, y) in self.knights:
            self.knights.remove((x, y))
        elif (x, y) in self.scouts:
            self.scouts.remove((x, y))

    def update_army(self, x0, y0, x1, y1):
        if (x0, y0) in self.spearmen:
            self.spearmen.remove((x0, y0))
            self.spearmen.append((x1, y1))
        elif (x0, y0) in self.archers:
            self.archers.remove((x0, y0))
            self.archers.append((x1, y1))
        elif (x0, y0) in self.knights:
            self.knights.remove((x0, y0))
            self.knights.append((x1, y1))
        elif (x0, y0) in self.scouts:
            self.scouts.remove((x0, y0))
            self.scouts.append((x1, y1))

    def can_recruit(self, army):
        if army == 'Spearman':
            if spearman_cost[0] > self.wood or spearman_cost[1] > self.food:
                return False
        elif army == 'Archer':
            if archer_cost[0] > self.wood or archer_cost[2] > self.gold:
                return False
        elif army == 'Knight':
            if knight_cost[1] > self.food or knight_cost[2] > self.gold:
                return False
        elif army == 'Scout':
            if scout_cost[0] > self.wood or scout_cost[1] > self.food or scout_cost[2] > self.gold:
                return False

        return True

    def move(self, army, x0, y0, x1, y1):
        army_tag = army[0]
        source = game_map[x0][y0]  # such as: '~~' or 'FF' or 'A2'
        destination = game_map[x1][y1] # such as: 'K1' or 'FF' or 'A2'

        if destination[0] == 'H' and int(destination[1]) != self.id:
            print("The army "+army+" captured the enemy’s capital.\n")
            name = input("What’s your name, commander?\n")
            print("\n***Congratulation! Emperor "+name+" unified the country in "+str(year)+".***")
            exit()

        elif destination == '~~':
            self.delete_army(x0, y0)

            game_map[x0][y0] = '  '

            print("We lost the army " + army + " due to your command!")
            return False

        elif destination == '  ':
            self.update_army(x0, y0, x1, y1)

            game_map[x1][y1] = game_map[x0][y0]
            game_map[x0][y0] = '  '

        elif destination == 'WW':
            self.wood += 2
            self.update_army(x0, y0, x1, y1)

            game_map[x1][y1] = game_map[x0][y0]
            game_map[x0][y0] = '  '

            print("Good. We collected 2 Wood.")

        elif destination == 'FF':
            self.food += 2
            self.update_army(x0, y0, x1, y1)

            game_map[x1][y1] = game_map[x0][y0]
            game_map[x0][y0] = '  '

            print("Good. We collected 2 Food.")

        elif destination == 'GG':
            self.gold += 2
            self.update_army(x0, y0, x1, y1)

            game_map[x1][y1] = game_map[x0][y0]
            game_map[x0][y0] = '  '

            print("Good. We collected 2 Gold.")

        elif destination[0] != army_tag and int(destination[1]) != self.id: # For source like 'A1' and destination like 'K2'
            if does_army_win(source[0], destination[0]):
                enemy = other_player.get_army_name(x1, y1)

                other_player.delete_army(x1, y1)
                self.update_army(x0, y0, x1, y1)

                game_map[x1][y1] = game_map[x0][y0]
                game_map[x0][y0] = '  '

                print("Great! We defeated the enemy " + enemy + "!")
            else:
                self.delete_army(x0, y0)

                game_map[x0][y0] = '  '

                print("We lost the army " + army + " due to your command!")
                return False

        elif destination[0] == army_tag and int(destination[1]) != self.id:  # For source like 'A1' and destination like 'A2'
            enemy = other_player.get_army_name(x1, y1)
            self.delete_army(x0, y0)
            other_player.delete_army(x1, y1)

            game_map[x0][y0] = '  '
            game_map[x1][y1] = '  '

            print("We destroyed the enemy " + enemy + " with massive loss!")
            return False

        return True

    def get_army_name(self, x0, y0):
        if (x0, y0) in self.spearmen:
            return "Spearman"
        elif (x0, y0) in self.archers:
            return "Archer"
        elif (x0, y0) in self.knights:
            return "Knight"
        elif (x0, y0) in self.scouts:
            return "Scout"


def does_army_win(army, opponent):
    if army == opponent:
        return False
    elif army == 'S':
        if opponent == 'A':
            return False
        else:
            return True
    elif army == 'A':
        if opponent == 'K':
            return False
        else:
            return True
    elif army == 'K':
        if opponent == 'S':
            return False
        else:
            return True
    elif army == 'T':
        return False


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
    print("Recruit Prices:\n  Spearman (S) - 1W, 1F\n  Archer (A) - 1W, 1G\n  Knight (K) - 1F, 1G\n  Scout (T) - 1W, 1F, 1G")


# Executes the given command
def execute_command(input):
    if input == 'DIS':
        display_map()
    elif input == 'PRIS':
        display_prices()
    elif input == 'QUIT':
        exit()
    else:
        return False


# Check recruitment validity (homebase free/resources free)
def homebase_free():
    if current_player.id == 1:
        return game_map[1][0] == '  ' or game_map[0][1] == '  ' or game_map[2][1] == '  ' or game_map[1][2] == '  '
    elif current_player.id == 2:
        return game_map[width-3][height-2] == '  ' or game_map[width-1][height-2] == '  ' or game_map[width-2][height-1] == '  ' or game_map[width-2][height-3] == '  '


# Check if input is adjacent to the homebase
def near_homebase(x, y):
    if current_player.id == 1:
        return (x, y) == (1, 0) or (x, y) == (0, 1) or (x, y) == (2, 1) or (x, y) == (1, 2)
    elif current_player.id == 2:
        return (x, y) == (width-3, height-2) or (x, y) == (width-1, height-2) or (x, y) == (width-2, height-1) or (x, y) == (width-2, height-3)


# Handles army recruitment
def handle_recruitment(user_input):
    if user_input == 'S':
        army = 'Spearman'
    elif user_input == 'A':
        army = 'Archer'
    elif user_input == 'K':
        army = 'Knight'
    elif user_input == 'T':
        army = 'Scout'

    if current_player.can_recruit(army) == False:
        print("Insufficient resources. Please try again.")
        return
    else:
        while True:
            army_position = input("\nYou want to recruit a " + army +". Enter two integers as format ‘x y’ to place your army.\n")

            if execute_command(army_position) == False:
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
                            current_player.recruit(army, int(x), int(y))

                            game_map[int(x)][int(y)] = user_input + str(current_player.id) # K1
                            print("You has recruited a " + army)

                            print("\n[Your Asset: Wood - " + str(current_player.wood) + " Food - " + str(current_player.food) + " Gold - " + str(current_player.gold) + "]")
                            break
                        else:
                            print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")


# Handles army movement
def handle_move(user_input):
    user_input = user_input.split()

    if len(user_input) != 4:
        print("Invalid move. Try again.")
    else:
        x0 = user_input[0]
        y0 = user_input[1]
        x1 = user_input[2]
        y1 = user_input[3]

        if type(int(x0)) != int or type(int(y0)) != int or type(int(x1)) != int or type(int(y1)) != int:
            print("Invalid move. Try again.")
        else:
            army = current_player.get_army_name(int(x0), int(y0))

            if army != 'Scout':
                if abs(int(x1) - int(x0)) > 1 or abs(int(y1) - int(y0)) > 1:
                    print("Invalid move. Try again.")
                else:
                    print("\nYou have moved " + army + " from " + str((int(x0), int(y0))) + " to " + str((int(x1), int(y1))) + ".")
                    current_player.move(army, int(x0), int(y0), int(x1), int(y1))
                    current_player.current_moves.append((int(x1), int(y1)))
            else:
                if abs(int(x1) - int(x0)) > 2 or abs(int(y1) - int(y0)) > 2:
                    print("Invalid move. Try again.")
                else:
                    print("\nYou have moved " + army + " from " + str((int(x0), int(y0))) + " to " + str((int(x1), int(y1))) + ".")
                    if int(x1)-int(x0) == 2:
                        if current_player.move(army, int(x0), int(y0), int(x0)+1, int(y1)):
                            current_player.move(army, int(x0)+1, int(y0), int(x1), int(y1))
                    elif int(x1) - int(x0) == -2:
                        if current_player.move(army, int(x0), int(y0), int(x0)-1, int(y1)):
                            current_player.move(army, int(x0)-1, int(y0), int(x1), int(y1))
                    elif int(y1) - int(y0) == 2:
                        if current_player.move(army, int(x0), int(y0), int(x1), int(y0)+1):
                            current_player.move(army, int(x0), int(y0)+1, int(x1), int(y1))
                    elif int(y1) - int(y0) == -2:
                        if current_player.move(army, int(x0), int(y0), int(x1), int(y0)-1):
                            current_player.move(army, int(x0), int(y0)-1, int(x1), int(y1))
                    else:
                        current_player.move(army, int(x0), int(y0), int(x1), int(y1))
                    current_player.current_moves.append((int(x1), int(y1)))




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
player1 = Player(1)
player2 = Player(2)
current_player = player1
other_player = player2

## Config loading complete ##


## Game started ##
print("Game Started: Little Battle! (enter QUIT to quit the game)\n")

display_map()
print("(enter DIS to display the map)\n")
display_prices()
print("(enter PRIS to display the price list)")

while True:
    print("\n-Year " + str(year) + "-")
    print("\n+++Player " + str(current_player.id) + "'s Stage: Recruit Armies+++")
    print("\n[Your Asset: Wood - " + str(current_player.wood) + " Food - "+ str(current_player.food) + " Gold - " + str(current_player.gold) + "]")

    ## Recruit army stage ##
    while True:
        if current_player.has_min_resources() == False:
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
    print("\n===Player " + str(current_player.id) + "'s Stage: Move Armies===")

    while True:
        if current_player.has_army_to_move() == False:
            print("\nNo Army to Move: next turn.")
            current_player.current_moves.clear()

            if current_player.id == 2:
                year += 1
            temp = current_player
            current_player = other_player
            other_player = temp
            break
        else:
            current_player.print_armies_to_move()

            user_input = input("\nEnter four integers as a format ‘x0 y0 x1 y1’ to represent move unit from (x0, y0) to (x1, y1) or ‘NO’ to end this turn.\n")

            if execute_command(user_input) == False:
                if user_input == 'NO':
                    current_player.current_moves.clear()

                    if current_player.id == 2:
                        year += 1
                    temp = current_player
                    current_player = other_player
                    other_player = temp
                    break
                else:
                    handle_move(user_input)
