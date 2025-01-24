import sys
from operator import add, mul, concat
from safe_IO import safe_get

def main():

    sys.setrecursionlimit(400096)

    if len(sys.argv) != 2:
        sys.exit("usage: python day7.py DATA_SET")
    data = safe_get(sys.argv[1])

    # set variable for function
    global opt
    opt = [add, mul, con]
    # make function that test all combinations of a set
    correct = []
    for line in data:
        print(line, end="")
        if opt_check(line[0], line[1:], 0):
            print(" True")
            correct.append(line[0])
        else:
            print(" False")

    print(sum(correct))

def opt_check(test, lst, itter):

    global opt

    #print("call base_to")
    comb = list(map(int, str(base_to(itter, 3))))
    while len(comb) != len(lst) - 1:
        comb = [0] + comb
    
    lst1 = lst[0]
    for i in range(len(comb)):
        #print(i, opt[comb[i]], lst1, lst[i + 1])
        lst1 = opt[comb[i]](lst1, lst[i + 1])
        #print(lst1)

    if lst1 == test:
        return True
    elif comb == [2] * len(comb):
        return False
    else:
        return opt_check(test, lst, itter + 1)

def base_to(base_10, new_base):
    quotient = base_10 // new_base
    remainder = base_10 % new_base
    if quotient == 0:
        return remainder
    return int(str(base_to(quotient, new_base)) + str(remainder))

def con(a, b):
    return int(concat(str(a), str(b)))

main()
