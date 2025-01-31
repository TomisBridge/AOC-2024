import sys
from operator import add, mul, concat, truediv, sub
from base_change import base_to, to_10
from safe_IO import safe_get

def main():

    # check for correct usage and import/format data
    if len(sys.argv) < 3:
        sys.exit(
                "\n ---------- usage: python day7.py DATA_SET OPERATORS ---------- \n"
                "\n ---------- OPERATORS -> add, mul, con, sub ---------- \n"
                )
    data = safe_get(sys.argv[1])

    # set variable with number of operators
    global opt_number
    opt_number = len(sys.argv[2:]) 

    # set global operators for check function
    global opt
    opt = []
    for i in range(opt_number):
        opt.append(eval(sys.argv[i + 2]))

    # 4782968 -> 14 digit base 3 numeber
    longest_string = 0
    for line in data:
        if len(line[2:]) > longest_string:
            longest_string = len(line[2:])
   
    base_from = int(str(opt_number) * longest_string)
    recurse_limit = to_10(base_from, opt_number)
    sys.setrecursionlimit(recurse_limit) 

    # itterate through all lines of the data and append to correct list if they pass
    correct = []
    for line in data:
        print(line, end="")
        if opt_check(line[0], line[1:], 0):
            print(" True")
            correct.append(line[0])
        else:
            print(" False")

    # print answer
    print(sum(correct))

# test all possible combination of operators and return bool
def opt_check(test, lst, itter):

    # set operator list
    global opt_number
    global opt

    # format the attempt itteration into a combination of operators to be tested
    comb = list(map(int, str(base_to(itter, opt_number))))
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
    elif comb == [opt_number - 1] * len(comb):
        return False

    # else recursively itterate through all posible combinations
    else:
        return opt_check(test, lst, itter + 1)

# concatination operator for operators list
def con(a, b):
    return int(concat(str(a), str(b)))

main()
