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

# function that tests if a given level is safe and returns a bool
# hand off to decending or acending functions
def safe_test(level):
    if level[0] - level[1] > 0:
        return ord_safe_test(level, 0, 1)
    elif level[0] - level[1] < 0:
        return ord_safe_test(level, 1, 0)
    else:
        False

# safe test for descending sets
# for part two add itterations for removed numbers
def ord_safe_test(level, asn, dsn):
    global itr
    for i in range(len(level) - 1):
        if not(0 < level[i + asn] - level[i + dsn] <= 3):
                
            # if first itteration
            if not(ord_safe_test(level, asn, dsn)) and (itr == 1):
                print("unsafe1: ", itr)
                level_mod = list(level)
                level_mod.remove(level[i])
                safe_test2(level, level_mod)

            # if second itteration
            elif not(safe2(level_mod)) and ((itr == 2) or (itr == 3)):  
                print("unsafe2: ", itr)
                level_mod = list(level)
                level_mod.remove(level[i + 1])
                safe_test2(level, level_mod)

       return False
    return True

# test first two numbers in list for safety
def safe_test2(level, level_mod):
    global itr
    itr += 1
    print("itr: ", itr, ", ", level, ", ", level_mod)

    # if first itteration
    if not(safe2(level)) and (itr == 1):
        print("unsafe1: ", itr)
        level_mod = list(level)
        level_mod.remove(level[0])
        safe_test2(level, level_mod)

    # if second itteration
    elif not(safe2(level_mod)) and ((itr == 2) or (itr == 3)):  
        print("unsafe2: ", itr)
        level_mod = list(level)
        level_mod.remove(level[1])
        safe_test2(level, level_mod)

    # if more then three itterations then return false
    elif itr > 3:
        itr = 0
        return False

    # if first two numbers pass acending and decending functions will still work
    else:
        itr = 0
        return safe_test(level)


# safe test for part 2
def safe2(level):
    print("safe2: ", level)
    if level == []:
        return False
    elif not(0 < abs(level[0] - level[1]) <= 3):
        print("False")
        return False
    print("True")
    return True



main()
