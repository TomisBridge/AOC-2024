#import pdb

def main():

    # import data specified file
#    breakpoint()
    target_file = input("input: ")
    data = format_AOC(target_file)

    print(data)

    # split data at \n to create a grid
    data_list = data.split("\n")
    data_list.pop(len(data_list) - 1)

    # initiate successful search count
    xmas_count = 0

    # search all combinations char and search for X's
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
#            breakpoint()
            if data_list[i][j] == "A" and check_x(data_list, i, j):
                xmas_count += 1
            print(i, j, xmas_count)

    # print answer
    print(xmas_count)
	
def format_AOC(target_file):

    #import data and store it in data as a str
    my_file = open(target_file, "r")
    data = []
    data = my_file.read()


    # close file
    my_file.close()

    return data

def check_x(data_list, i, j):

    for x in range(3):
         one = ( i - 1 ) + x
         for y in range(3):
             two = ( j - 1 ) + y
             if not(0 <= one <= len(data_list) - 1) or not(0 <= two <= len(data_list[x]) - 1):
                 return False

    corners = [data_list[i - 1][j - 1], data_list[i + 1][j - 1], data_list[i - 1][j + 1], data_list[i + 1][j + 1]]
    print(corners)
    if corners.count("M") == 2 and corners.count("S") == 2:
        if corners != ['M', 'S', 'S', 'M'] and corners != ['S', 'M', 'M', 'S']:
            print(corners, "True")
            return True
    return False

main()
