from safe_IO import safe_get 
from re import search
from my_map import a_map, position
import sys

def main():

    # check to ensure a file name has been give
    if len(sys.argv) != 2:
        sys.exit("\n ------------ usage: python day6.py FILE_NAME ------------ \n")
 
    # asign data from file to lab_map variable
    lab_map = safe_get(sys.argv[1])
    print_map(lab_map)
    print("")

    # find the location of the gaurd and assign it to the gaurd variable
    gaurdxy = find_gaurd(lab_map) 
    gaurd = position(lab_map, lab_map[gaurdxy[0]][gaurdxy[1]], gaurdxy[0], gaurdxy[1])
    gaurd.mark()

    loops = 0
    test = 0
    grid_loop = []

    while True:
        print(test)
        test += 1
        if not(gaurd.in_map(gaurd.nextp())):
            break
        elif gaurd.at_location(gaurd.nextp()) == "#":
            gaurd.turn()
            gaurd.mark()
        else:
            if loop_check(gaurd):
                loops += 1
            gaurd.move()
            gaurd.mark()

    gaurd.print_map()
    print(loops)
    

# find the gaurd return [-1, -1] if the gaurd cannot be found
def find_gaurd(lab_map):
    for row in range(len(lab_map)):
        for column in range(len(lab_map[row])):
            if bool(search(r"<|\^|>|v", lab_map[row][column])):
                return [row, column]
    return [-1, -1]

def loop_check(gaurd):
    ghost = position(gaurd.grid, gaurd.direction, gaurd.x, gaurd.y)
    ghost.turn()
    brick = 0
    while True:
        if not(ghost.in_map(ghost.nextp())): 
            break
        elif brick > 100:
            break
        elif not(ghost.at_location(ghost.nextp())) != "#":
            brick += 1
            ghost.turn()
        else:
            if ghost.at_location(ghost.nextp()).find(ghost.direction) > 0:
                del ghost
                return True
            ghost.move()
    del ghost
    return False

# print map in a more estheticly pleasing way
def print_map(map):
    for line in map:
        print(line)

if __name__ == "__main__":
    main()
