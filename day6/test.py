from day6 import find_gaurd
import sys
from safe_IO import safe_get
from my_map import position, a_map

def main():

    lab_map = safe_get(sys.argv[1])
    gaurdxy = find_gaurd(lab_map)
    gaurd = position(lab_map, lab_map[gaurdxy[0]][gaurdxy[1]], gaurdxy[0], gaurdxy[1])

    print(gaurd.in_map([-1, -1]))
    
    while True:
        key_input = input("command: ")
        if key_input == "move":
            gaurd.move()
            gaurd.mark()
            gaurd.print_map()
        if key_input == "turn":
            gaurd.turn()
            gaurd.mark()
        if key_input == "location":
            print(gaurd.location())
        if key_input == "at_location":
            print(gaurd.at_location(gaurd.location()))
        if key_input == "print_map":
            gaurd.print_map()
        if key_input == "nextp":
            print(gaurd.nextp())
        if key_input == "in_map":
            print(gaurd.in_map(gaurd.nextp()))
        if key_input == "q":
            break

            


main()
