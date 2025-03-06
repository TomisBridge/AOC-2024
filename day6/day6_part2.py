from safe_IO import safe_get, dump_info
from re import search
from my_map import a_map, position
from copy import deepcopy, copy
from PIL import Image
import sys

def main():

    # check to ensure a file name has been give
    if len(sys.argv) != 2:
        sys.exit("\n ------------ usage: python day6.py FILE_NAME ------------ \n")
 
    # asign data from file to lab_map variable
    lab_map = safe_get(sys.argv[1])

    # find the location of the gaurd and assign it to the gaurd variable
    gaurdxy = find_gaurd(lab_map) 
    gaurd = position(lab_map, lab_map[gaurdxy[0]][gaurdxy[1]], gaurdxy[0], gaurdxy[1])
    gaurd.mark()

    global map_pic
    map_pic = Image.new(mode="RGB", size=[len(gaurd.grid), len(gaurd.grid[0])], color=(100, 100, 100))
    map_pic.putpixel((gaurd.x, gaurd.y), (0, 255, 0))
    for i in range(len(gaurd.grid)):
        for j in range(len(gaurd.grid[0])):
            if gaurd.grid[i][j] == "#":
                map_pic.putpixel((i, j), (255, 0, 0))
                
    loops = 0
    global grid_loop
    grid_loop = 0
    global false
    false = 0
    global blocked
    blocked = []

    blocked.append(gaurd.location())

    while True:
        print(loops, end="\r")
        if not(gaurd.in_map(gaurd.nextp())):
            break
        elif gaurd.at_location(gaurd.nextp()) == "#":
            gaurd.turn()
            gaurd.mark()
            map_pic.putpixel((gaurd.x, gaurd.y), (0, 0, 0))
        else:
            if loop_check(gaurd) and gaurd.nextp() != gaurdxy:
                loops += 1
            gaurd.move()
            gaurd.mark()
            map_pic.putpixel((gaurd.x, gaurd.y), (0, 0, 0))

    print(f"\n ---------- loops: {loops} ---------- \n")

# find the gaurd return [-1, -1] if the gaurd cannot be found
def find_gaurd(lab_map):
    for row in range(len(lab_map)):
        for column in range(len(lab_map[row])):
            if bool(search(r"<|\^|>|v", lab_map[row][column])):
                return [row, column]
    return [-1, -1]

def loop_check(gaurd):
    global grid_loop
    global map_pic
    global blocked
    global false

    blank = deepcopy(map_pic)

    ghost = position(deepcopy(gaurd.grid), copy(gaurd.direction), copy(gaurd.x), copy(gaurd.y))
    if not(ghost.nextp() in blocked):
        ghost.block(ghost.nextp())
    blocked.append(ghost.nextp())
    blank.putpixel(ghost.nextp(), (255, 255, 0))

    while True:
        if not(ghost.in_map(ghost.nextp())): 
            false += 1
            blank.putpixel((ghost.x, ghost.y), (0, 0, 255))
            blank = blank.resize((1000, 1000), Image.Resampling.BOX)
            blank.save(f"found_loops/false{false}.jpg")
            break
        elif ghost.at_location(ghost.nextp()) == '#':
            blank.putpixel((ghost.x, ghost.y), (0, 255, 255))
            ghost.turn()
            ghost.mark()
        elif ghost.at_location(ghost.nextp()).find(ghost.direction) > 0:
            grid_loop += 1
            blank.putpixel((ghost.x, ghost.y), (0, 0, 255))
            blank = blank.resize((1000, 1000), Image.Resampling.BOX)
            blank.save(f"found_loops/loop{grid_loop}.jpg")
            del ghost
            return True
        else:
            ghost.move()
            ghost.mark()
            blank.putpixel((ghost.x, ghost.y), (255, 255, 255))

    del ghost
    return False

# print map in a more estheticly pleasing way
def print_map(map):
    for line in map:
        print(line)

if __name__ == "__main__":
    main()
