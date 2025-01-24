import sys
from operator import add, mul, concat
from safe_IO import safe_get

def main():

    # 4782968 -> 14 digit base 3 numeber
    sys.setrecursionlimit(4782968) 

    # check for correct usage and import/format data
    if len(sys.argv) != 2:
        sys.exit("usage: python day7.py DATA_SET")
    data = safe_get(sys.argv[1])

    # set global operators for check function
    global opt
    opt = [add, mul, con]

    # itterate through all lines of the data and append to correct list of they pass
    correct = []
    for line in data:
        print(line, end="")
        if opt_check(line[0], line[1:], 0):
            print(" True")
            correct.append(line[0])
        else:
            print(" False")

    # print anser
    print(sum(correct))

# test all possible combination of operators and return bool
def opt_check(test, lst, itter):

    # set operator list
    global opt

    # format the attempt itteration into a combination of operators to be tested
    comb = list(map(int, str(base_to(itter, 3))))
    while len(comb) != len(lst) - 1:
        comb = [0] + comb
    
    # perform each operation in comb from left to right
    lst1 = lst[0]
    for i in range(len(comb)):
        lst1 = opt[comb[i]](lst1, lst[i + 1])

    # if the comb is successfull return True
    if lst1 == test:
        return True

    # if the comb if at its final combination and is unsuccessful return False
    elif comb == [2] * len(comb):
        return False

    # else recursively itterate through all posible combinations
    else:
        return opt_check(test, lst, itter + 1)

# convert base 10 number to number of base 2 -> 9
def base_to(base_10, new_base):
    quotient = base_10 // new_base
    remainder = base_10 % new_base
    if quotient == 0:
        return remainder
    return int(str(base_to(quotient, new_base)) + str(remainder))

# concatination operator for operators list
def con(a, b):
    return int(concat(str(a), str(b)))

main()
