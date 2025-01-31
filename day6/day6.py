from safe_IO import safe_get 
from re import search
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("\n ------------ usage: python day6.py FILE_NAME ------------ \n")
 

    lab_map = safe_get(sys.argv[1])
    print(lab_map)
    gaurd = find_gaurd(lab_map)
    print(gaurd)
    lab_map2 = move(lab_map, gaurd, -1, -1)
    print(lab_map2)

def find_gaurd(lab_map):
    for row in range(len(lab_map)):
        for column in range(len(lab_map[row])):
            if bool(search(r"<|\^|>|v", lab_map[row][column])):
                return [row, column]
    return [-1, -1]

def move(lab_map, gaurd, x, y):
    lab_map[gaurd[0]] = lab_map[gaurd[0]].replace(lab_map[gaurd[0]][gaurd[1]], "X")
    return lab_map


main()
