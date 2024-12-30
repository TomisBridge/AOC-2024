# set global target and counter variables
global counter
counter = 0
global target
target = ['X', 'M', 'A', 'S']

def main():

    # import data specified file
    target_file = input("input: ")
    data = format_AOC(target_file)

    print(data)

    # split data at \n to create a grid
    data_list = data.split("\n")
    data_list.pop(len(data_list) - 1)

    # initiate global variables
    global counter
    global target

    # initiate successful search count
    xmas_count = 0

    # search all combinations char and search for X's
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            xmas_count += search(data_list, i, j)
            print(i, j, xmas_count)

    # print answer
    print(xmas_count)
	
def format_AOC(target_file):

    #import data and store it in data as a str
    my_file = open(target_file, "r")
    data = []
    data = my_file.read()


    # close file
    my_file.close()

    return data

def search(data_list, i, j):

    # initiate global counter variable
    global counter
    global target

    # if value at given corrordinate are an X proceed to recursive search
    if data_list[i][j] == "X":
        counter += 1 # incriment counter to change target to M
        return rec_search(data_list, i, j)

    # if the value at given corrordinance isnt an X return False
    return False


def rec_search(data_list, i, j):

    # setting global target tnad counter variables
    global counter
    global target
    
    # set tally for successful searches
    tally = 0

    # check serounding characters for the next charater in the target set
    seround = serounding(data_list, i, j)
    for k in range(len(seround)):
        if seround[k][0] == target[counter]:
            counter += 1

            # search in desired direction starting at i, j and proceeding in x, y direction
            print(seround[k], data_list[i][j], i, j)
            print(seround[k][1], seround[k][2], seround[k][1] - i, seround[k][2] - j)
            if direct_search(data_list, seround[k][1], seround[k][2], seround[k][1] - i, seround[k][2] - j):
                tally += 1
                print(tally, "tally += 1")
            else:
                counter -= 1


    counter = 0
    return tally


def direct_search(data_list, i, j, x, y):
    
    # set global variables
    global target
    global counter

    # check for ensure search is not out of range
    if i + x == len(data_list) or i + x < 0 or j + y == len(data_list[i]) or j + y < 0:
        return False

    # search for recursively search through all directions that an M was for
    elif data_list[i + x][j + y] == target[counter]:
        if counter == 3:
            print(target[counter], counter, i + x, j + y)
            counter = 1
            return True
        else:
            print(target[counter], counter, i + x, j + y)
            counter += 1
            return direct_search(data_list, i + x, j + y, x, y)	
    else:
        return False

def serounding(test_list, x, y):
    serounding = []
    for i in range(3):
        one = ( x - 1 ) + i
        for j in range(3):
            two = ( y - 1 ) + j
            if 0 <= one <= len(test_list) - 1 and 0 <= two <= len(test_list[x]) - 1:
                serounding.append([test_list[one][two], one, two])
    return serounding


main()
