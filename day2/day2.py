# advent of code day two part one

def main():

    # retrieve data
    data = format_AOC_day2(input("input file name: "))

    # sum the safe list items
    safe = 0
    for level in data:
        if safe_test(level):
            safe += 1

    print(safe)

# import datat and format it into a list of lists
def format_AOC_day2(target_file):

    #import data and store it in data as a str
    my_file = open(target_file, "r")
    data = []
    data = my_file.read()

    # split data into a single list splitting at \n and removing spaces
    data_into_list = data.split("\n")
    data_into_lists = []

    # screen for empty lists then split list in sub lists at spaces
    for lst in data_into_list:
        if lst != "":
            data_into_lists.append(lst.split(" "))

    # convert chars to ints
    num_list = []
    for lst in data_into_lists:
        num_list.append(list(map(int, lst)))
    
    return num_list

    # close file
    my_file.close()

# function that tests if a given level is safe and returns a bool
# hand off to decending or acending functions
def safe_test(level):
    if level[0] - level[1] > 0:
        return dsn_safe_test(level)
    elif level[0] - level[1] < 0:
        return asn_safe_test(level)
    else:
        False

# safe test for descending sets
def dsn_safe_test(level):
    for i in range(len(level) - 1):
        if not(0 < level[i] - level[i + 1] <= 3):
            return False
    return True

# safe test for ascending sets
def asn_safe_test(level):
    for i in range(len(level) - 1):
        if not(0 < level[i + 1] - level[i] <= 3):
            return False
    return True
          

main()
