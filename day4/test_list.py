def main():

	test_list = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]

	print(test_list)

	print(test_list[1][2])

	x = int(input("input x: "))
	y = int(input("input y: "))

	seround = serounding(test_list, x, y)
	
	print(seround)

def serounding(test_list, x, y):
	serounding = []
	for i in range(3):
		one = ( x - 1 ) + i
		for j in range(3):
			two = ( y - 1 ) + j
			print(one, two)
			if 0 <= one <= len(test_list) - 1 and 0 <= two <= len(test_list[x]) - 1:
				serounding.append([one, two, test_list[one][two]]) 
	return serounding

main()
