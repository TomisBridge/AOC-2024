# import regular expression library
import re

def main():
    
    # import data
    data = format_AOC_day3(input("input name: "))
    print(data)

    # split into list in front of d and m
    data_list = data.replace("d", " d").replace("m", " m").split(" ")

    print(data_list)

    # filter match mul(#,#), do(), don't() and append to filtered list
    filtered = []
    for item in data_list:
        print(item)
        result = re.match(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", item)
        if result != None:
            filtered.append(result.group(0))

    print(filtered)

    toggle = 1
    tally = 0

    # evaluate each item in list
    for item in filtered:

        # toggle between 1 and 0 for do and dont items
        if item == "don't()":
            toggle = 0
        elif item == "do()":
            toggle = 1

        # tally good data only when toggle is 1
        else:
            if toggle == 1:
                pairs = re.findall(r"[0-9]{1,3}", item)
                print(pairs)
                tally += int(pairs[0]) * int(pairs[1])

    print(tally)

# import data function
def format_AOC_day3(target_file):

    #import data and store it in data as a str
    my_file = open(target_file, "r")
    data = []
    data = my_file.read()


    # close file
    my_file.close()
    
    return data

main()
