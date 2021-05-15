width = 5
height = 5
game_map=[['WW', '  ', '  ', '  ', '  '],
          ['  ', 'H1', '  ', '  ', 'GG'],
          ['  ', '  ', '  ', '  ', '  '],
          ['  ', '  ', '  ', 'H2', '  '],
          ['  ', 'FF', '  ', '  ', '  ']]

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