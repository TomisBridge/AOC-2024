def main():

    # request file name from user
    target_file = input("insert file name: ")

    # set data variable
    data = format_AOC_day1(target_file)

    # create a single list of left and right values
    left_list = []
    for pair in data:
        left_list.append(pair[0])
    sorted_left_list = sorted(left_list)

    right_list = []
    for pair in data:
        right_list.append(pair[1])
    sorted_right_list = sorted(right_list)

    # create a list of the differences between the left and right sorted list
    diff_list = abs_diff(sorted_left_list, sorted_right_list)

    # sum the list and print/return the answer
    answer = sum(diff_list)
    print(answer)
    return answer
    

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





main()

