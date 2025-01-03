def main():

    # import data specified file
    target_file = input("input: ")
    data = format_AOC(target_file)

    # split data at \n to create a grid
    data_list = data.split("\n")
    data_list.pop(len(data_list) - 1)

    # initiate successful search count
    xmas_count = 0

    # search all combinations char and search for X's
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            if data_list[i][j] == "A" and check_x(data_list, i, j):
                xmas_count += 1

    # print answer
    print("\n----------> The data set contains", xmas_count, "X-MAS's <----------\n")
	
# import data and format for question
def format_AOC(target_file):

    #import data and store it in data as a str
    my_file = open(target_file, "r")
    data = my_file.read()


    # close file
    my_file.close()

    return data

# check if location of an A satisties the X pattern decribed by part two of problem four
def check_x(data_list, i, j):

    # check for any data points out of range. return False if out of range
    for x in range(3):
         one = ( i - 1 ) + x
         for y in range(3):
             two = ( j - 1 ) + y
             if not(0 <= one <= len(data_list) - 1) or not(0 <= two <= len(data_list[x]) - 1):
                 return False

    # create list that contains the diagnaly adjacent characters
    corners = [data_list[i - 1][j - 1], data_list[i + 1][j - 1], data_list[i - 1][j + 1], data_list[i + 1][j + 1]]
    
    # check for two Ms and two Ss
    if corners.count("M") == 2 and corners.count("S") == 2:

        # eliminate bad patters
        if corners != ['M', 'S', 'S', 'M'] and corners != ['S', 'M', 'M', 'S']:
            return True

    #return False if no good pattern found
    return False

main()
