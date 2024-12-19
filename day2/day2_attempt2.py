# advent of code day two part one
def main():

    # retrieve data
    data = format_AOC_day2(input("input file name: "))
    
    # sum the safe list items
    safe = 0
    for level in data:
        print("level: ", level)
        if safe_test2(level):
            safe += 1
            print("level safe:", level, "current safe count: ", safe)
        elif last_char_test(level):
            safe += 1
            print("level safe:", level, "current safe count: ", safe)
        else:
            print("level unsafe", level, "current safe count: ", safe)
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

# if safe test returns test the level again remove on char at a time
def safe_test2(level):

    # test if it passes without removing char
    if safe_test(level):
        return True

    # if it does not pass test each possible list with one char removed
    else:
        for i in range(len(level) - 1):
            print("char removed: ", i, "from level: ", level)
            level_mod = list(level)
            level_mod.pop(i)
            if safe_test(level_mod):
                return True

    # return false if all above tests do not pass
    return False
                       
# quick and dirty fix for above function not testing the last char
def last_char_test(level):
    level.pop()
    return safe_test(level)

# function that tests if a given level is safe and returns a bool
# hand off to decending or acending functions
def safe_test(level):
    if level[0] - level[1] > 0:
        return ord_safe_test(level, 0, 1) # decending list
    elif level[0] - level[1] < 0:
        return ord_safe_test(level, 1, 0) # asending list
    else:
        False
    
       
# safe test for descending sets
# for part two add itterations for removed numbers
def ord_safe_test(level, asn, dsn):

    for i in range(len(level) - 1):

        # if a pair is out of range modify level
        if not(0 < level[i + asn] - level[i + dsn] <= 3):
            return False
    
    return True

main()
