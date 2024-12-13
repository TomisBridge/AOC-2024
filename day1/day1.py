def main():

    # request file name from user
    target_file = input("insert file name: ")

    # set data variable
    data = format_AOC_day1(target_file)

    # create a single list of left and right values
    sorted_left_list = split_sort(data, 0)

    sorted_right_list = split_sort(data, 1)

    # create a list of the differences between the left and right sorted list
    diff_list = abs_diff(sorted_left_list, sorted_right_list)

    # sum the list and print/return the answer
    answer = sum(diff_list)
    print("part one: ", answer)
   
    # day 1 part 2 compare left list to right list as outlined in problem 
    sim_list = []
    for i in sorted_left_list:
        sim_list.append(sim_func(i, sorted_right_list))

    # sum the similarity list
    answer2 = sum(sim_list)
    print("part two: ", answer2)

# import datat and format it into a list of lists
def format_AOC_day1(target_file):

    #import data and store it in data as a str
    my_file = open(target_file, "r")
    data = []
    data = my_file.read()

    # split data into a single list splitting at \n
    data_into_list = data.split("\n")
    
    # split data into a list of list splitting at 3 spaces. final format eg. [[1, 2], [3, 4], [5,6]]
    data_into_lists = []
    for pair in data_into_list:
        if pair != "":
            data_into_lists.append(pair.split("   "))
    return data_into_lists
    
    # close file
    my_file.close()

# take the absolute value of the defference of the two inputs formatted as a list [1, 2]
def abs_diff(left, right):
    diff_list = []
    for i in range(len(left)):
        diff_list.append(abs(int(left[i]) - int(right[i])))
    return diff_list

# takes a list of pairs (eg. [[1, 2], [3, 4], [5,6]]) and a 0 or 1 for left or right. outputs a sorted list of the desired side.
def split_sort(data, side):
    lst = []
    for pair in data:
        lst.append(pair[side])
    sorted_list = sorted(lst)
    return sorted_list

# apply the similarity comparison from problem 2
def sim_func(i, lst):
    return (int(i) * lst.count(i))


main



main



main



main



main()

