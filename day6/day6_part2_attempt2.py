from safe_IO import safe_get 
from re import search
from my_map import a_map, position
from copy import deepcopy, copy
import sys

def main():

    # check to ensure a file name has been give
    if len(sys.argv) != 2:
        sys.exit("\n ------------ usage: python day6.py FILE_NAME ------------ \n")
 
    # asign data from file to lab_map variable
    lab_map = safe_get(sys.argv[1])

    # find the location of the gaurd and assign it to the gaurd variable
    gaurdxy = find_gaurd(lab_map) 

    loops = 0

    for i in range(len(lab_map)):
        for j in range(len(lab_map[i])):

            gaurd = position(deepcopy(lab_map), copy(lab_map[gaurdxy[0]][gaurdxy[1]]), copy(gaurdxy[0]), copy(gaurdxy[1]))
            gaurd.block([i, j])

            while True:
                
                if not(gaurd.in_map(gaurd.nextp())): 
                    del gaurd
                    break

                elif gaurd.at_location(gaurd.nextp()) == "#":
                    gaurd.turn()
                    
                elif gaurd.at_location(gaurd.nextp()).find("#") > 0:
                    gaurd.turn()

                elif gaurd.at_location(gaurd.nextp()).find(gaurd.direction) > 0:
                    del gaurd
                    loops += 1
                    break

                else:
                    gaurd.move()
                    gaurd.mark()
                    
    print(loops)

# find the gaurd return [-1, -1] if the gaurd cannot be found
def find_gaurd(lab_map):
    for row in range(len(lab_map)):
        for column in range(len(lab_map[row])):
            if bool(search(r"<|\^|>|v", lab_map[row][column])):
                return [row, column]
    return [-1, -1]

# print map in a more estheticly pleasing way
def print_map(map):
    for line in map:
        print(line)

if __name__ == "__main__":
    main()
