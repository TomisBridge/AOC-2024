# advent of code day two part one
def main():


    # set itteration counter variable for the safe2 function
    global itr
    itr = 0

    # retrieve data
    data = format_AOC_day2(input("input file name: "))
    
    # sum the safe list items
    safe2 = 0
    for level in data:
        if safe_test2(level, []):
            safe2 += 1
            print("level safe:", level, "current safe count: ", safe2)
        else:
            print("level unsafe", level, "current safe count: ", safe2)
    print(safe2)


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

# test first two numbers in list for safety
def safe_test2(level, level_mod):

    global itr
    # if first itteration
    if not(safe2(level)) and itr == 0:
        return mod(level, 0, safe_test2)

    elif not(safe2(level_mod)) and itr > 0:
        return mod(level, 0, safe_test2)

    # if first two numbers pass, acending and decending functions will still work
    else:
        if itr == 0:
            return safe_test(level, [])
        elif itr > 0:
            itr = 2 # level has already been modified. itr = 2 forces a fail in the mod function
            return safe_test(level, level_mod)

# safe test for part 2
def safe2(level):
    if level == []:
        return False
    elif not(0 < abs(level[0] - level[1]) <= 3):
        return False
    return True
 
# function that tests if a given level is safe and returns a bool
# hand off to decending or acending functions
def safe_test(level, level_mod):
    if itr == 0:
        if level[0] - level[1] > 0:
            return ord_safe_test(level, 0, 1, level_mod) # decending list
        elif level[0] - level[1] < 0:
            return ord_safe_test(level, 1, 0, level_mod) # asending list
        else:
            False
        
    if itr > 0:
        if level_mod[0] - level_mod[1] > 0:
            return ord_safe_test(level, 0, 1, level_mod) # decending list
        elif level_mod[0] - level_mod[1] < 0:
            return ord_safe_test(level, 1, 0, level_mod) # asending list
        else:
            False
        
# safe test for descending sets
# for part two add itterations for removed numbers
def ord_safe_test(level, asn, dsn, level_mod):

    global itr

    if itr == 0:
        # test all number pairs in level
        for i in range(len(level) - 1):

            # if a pair is out of range modify level and retest
            if not(0 < level[i + asn] - level[i + dsn] <= 3):
                return mod(level, i, safe_test) # if itr > 1 mod will not perform any more tests
        itr = 0
        return True

    else:

        # test all number pairs in level
        for i in range(len(level_mod) - 1):

            # if a pair is out of range modify level and retest
            if not(0 < level_mod[i + asn] - level_mod[i + dsn] <= 3):
                return mod(level, (i + 1), safe_test) # if itr > 1 mod will not perform any more tests
        itr = 0
        return True


# move one of the possible faulty numbers and return level to the desired function
def mod(level, i, func):
    # check if itteration is greater then one both modifications have been performed
    global itr
    print("mod", level, i, func, "itr: ", itr)
    if itr > 1:
        itr = 0
        return False

    # copy original list to modify
    level_mod = list(level)

    # if on the first itteration remove first of suspect numbers
    if itr == 0:
        level_mod.pop(i)

    # if on the second itteration remove first of suspect numbers
    elif itr == 1:
        level_mod.pop(i + 1)

    # incriment itteration counter
    itr += 1

    # return modified values to desired test function
    return func(level, level_mod)


main()
