from safe_IO import safe_get 
from re import search
import sys

def main():

    # check to ensure a file name has been give
    if len(sys.argv) != 2:
        sys.exit("\n ------------ usage: python day6.py FILE_NAME ------------ \n")
 
    # asign data from file to lab_map variable
    lab_map = safe_get(sys.argv[1])
    print_map(lab_map)

    # move the gaurd through positions until they leave the map
    while True:

        # find the location of the gaurd and assign it to the gaurd variable
        gaurd = find_gaurd(lab_map) # find_gaurd equation returns [-1, -1] if it cant find the gaurd

        # check that the gaurd is still on the map
        if gaurd == [-1, -1]:
            break

        # check if the next position is a # and change gard direction if it is
        elif in_range(next_position(gaurd, lab_map), lab_map):
            nextp = next_position(gaurd, lab_map)
            if lab_map[nextp[0]][nextp[1]] == "#":
                toggle(gaurd, lab_map)
        move(lab_map, gaurd)

    # print completed lab map
    print(lab_map)

    # count the Xs of the map
    count = 0
    for line in lab_map:
        for position in line:
            if position == "X":
                count += 1

    # print the final count
    print(count)

# change the postition of the gaurd
def toggle(gaurd, lab_map):
    directions = ["<", "^", ">", "v"]
    current_gaurd = lab_map[gaurd[0]][gaurd[1]]
    current_gaurd_number = directions.index(current_gaurd)
    if current_gaurd_number == 3:
        lab_map[gaurd[0]][gaurd[1]] = directions[0]
    else:
        lab_map[gaurd[0]][gaurd[1]] = directions[current_gaurd_number + 1]

# find the gaurd return [-1, -1] if the gaurd cannot be found
def find_gaurd(lab_map):
    for row in range(len(lab_map)):
        for column in range(len(lab_map[row])):
            if bool(search(r"<|\^|>|v", lab_map[row][column])):
                return [row, column]
    return [-1, -1]

# check weather the given position is still on the map
def in_range(new_position, lab_map):
    if 0 <= new_position[0] <= len(lab_map) - 1 and 0 <= new_position[1] <= len(lab_map[0]) - 1:
        return True
    else:
        return False

# move the gaurd one position in the direction they are facing
def move(lab_map, gaurd):
    new_position = next_position(gaurd, lab_map)
    if in_range(new_position, lab_map):
        lab_map[new_position[0]][new_position[1]] = lab_map[gaurd[0]][gaurd[1]]
    lab_map[gaurd[0]][gaurd[1]] = "X"
    return lab_map

# give the location of the next position the gaurd will move
def next_position(gaurd, lab_map):
    gaurd_direction = lab_map[gaurd[0]][gaurd[1]]
    match gaurd_direction:
        case "<":
            x = 0
            y = -1
        case "^":
            x = -1
            y = 0
        case ">":
            x = 0
            y = 1
        case "v":
            x = 1
            y = 0

    new_position = [gaurd[0] + x, gaurd[1] + y]
    return new_position

# print map in a more estheticly pleasing way
def print_map(map):
    for line in map:
        print(line)

if __name__ == "__main__":
    main()
