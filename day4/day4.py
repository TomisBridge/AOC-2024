# set global target and counter variables
global counter
counter = 0
global target
target = ['X', 'M', 'A', 'S']

def main():

    # import data specified file
    target_file = input("input: ")
    data = format_AOC(target_file)

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

    # print answer
    print("\n----------> The data set contains", xmas_count, "XMAS's <----------\n")
	
def format_AOC(target_file):

    #import data and store it in data as a str
    my_file = open(target_file, "r")
    data = my_file.read()


    # close file
    my_file.close()

    return data

# check if input location contains an X and search for MAS using rec_search
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


# search serounding locations for M and when found use direct_search (disrectional search) to check for AS
def rec_search(data_list, i, j):

    # setting global target tnad counter variables
    global counter
    global target
    
    # set tally for successful searches
    tally = 0

    # check serounding characters for the next charater in the target set if the correct character is found incriment the counter
    seround = serounding(data_list, i, j)
    for k in range(len(seround)):
        counter = 1
        if seround[k][0] == target[counter]:
            counter += 1

            # search in desired direction starting at i, j and proceeding in x, y direction
            if direct_search(data_list, seround[k][1], seround[k][2], seround[k][1] - i, seround[k][2] - j):
                tally += 1
            else:
                counter -= 1


    # set counter to 0 and return tally
    counter = 0
    return tally


# search function that recusively searches in the direction established by the first two characters
def direct_search(data_list, i, j, x, y):
    
    # set global variables
    global target
    global counter

    # check for ensure search is not out of range
    if i + x == len(data_list) or i + x < 0 or j + y == len(data_list[i]) or j + y < 0:
        return False

    # search for recursively search through all directions that an M was for
    elif data_list[i + x][j + y] == target[counter]:

        # if the counter is at 3 then the correct word has been found return True
        if counter == 3:
            return True

        # if the counter is not at three increment the counter and recursively search with this function
        else:
            counter += 1
            return direct_search(data_list, i + x, j + y, x, y)	

    # if the above two statements are false then the string does not contain xmas
    else:
        return False

def serounding(data_list, i, j):

    # create empty list
    serounding = []

    # loop through all positions around the given location in the matrix
    for x in range(3):
        column = ( i - 1 ) + x
        for y in range(3):
            row = ( j - 1 ) + y

            # check if the given location is outside of the matrix
            if 0 <= column <= len(data_list) - 1 and 0 <= row <= len(data_list[x]) - 1:

                # if the location exists append it to seround in format [value, calumn, row]
                serounding.append([data_list[column][row], column, row])

    # return serounding values
    return serounding


main()
