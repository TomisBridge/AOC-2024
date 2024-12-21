# set global target and counter variables
global counter
counter = 0
global target
target = ['X', 'M', 'A', 'S']

def main():

	# import data specified file
	target_file = input("input: ")
	data = format_AOC(target_file)

	print(data)
	
	# split data at \n to create a grid
	data_list = data.split("\n")
	data_list.pop(len(data_list) - 1)

	# initiate global variables
	global counter
	global target

	# initiate successful search count
	xmas_count = 0

	# search all combinations char and search for X's
	for i in range(len(data_list) - 1):
		for j in range(len(data_list[i]) - 1):
			if search(data_list, i, j):
				xmas_count += 1
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

def search(data_list, i, j):

	# initiate global counter variable
	global counter
	global target

	# if value at given corrordinate are an X proceed to recursive search
	if data_list[i][j] == "X":
		print(target[counter], i, j, end=", ")
		counter += 1 # incriment counter to change target to M
		return rec_search(data_list, i, j)

	# if the value at given corrordinance isnt an X return False
	return False


def rec_search(data_list, i, j):
	global counter
	global target
	seround = serounding(data_list, i, j)
	for i in range(len(seround) - 1):
		if seround[i][2] == target[counter]:
			if counter == 3:
				print(target[counter], i, j, end=", ")
				counter = 0
				return True
			else:
				print(target[counter], i, j, end=", ")
				counter += 1
				return rec_search(data_list, seround[i][0], seround[i][1])	

def serounding(test_list, x, y):
        serounding = []
        for i in range(3):
                one = ( x - 1 ) + i
                for j in range(3):
                        two = ( y - 1 ) + j
                        if 0 <= one <= len(test_list) - 1 and 0 <= two <= len(test_list[x]) - 1:
                                serounding.append([one, two, test_list[one][two]])
        return serounding


main()

