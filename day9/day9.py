import sys
import time
from safe_IO import safe_get
from compressor import data_list

#note start time to get full run time at end of program
start_time = time.time()

def main():

    #use safe get to get and format data
    data = safe_get(sys.argv[1])

    #set global variables neccessary for flip_flop function
    global current_block
    current_block = 0
    global flip_flop
    flip_flop = file_length

    #initiate empty list to wright to with flip_flop function
    uncompressed = []

    # create list of in correct format
    # flip flop function alternate between file length and free space function
    # by use of the toggle function
    for number in data:
        uncompressed += (flip_flop(number))
        toggle()

    # initiate object to keep track of the element of the list being compared
    # using the start and end values
    comp_obj = data_list(uncompressed, 0, len(uncompressed) - 1)

    # compare contents of data at start and end possitions
    while True:

        # create an approximate count down at program takes some time with full data set
        print(comp_obj.end - int(len(comp_obj.data)/1.9), "      ", end="\r")

        # break out of loop once start possition equals end possition
        if comp_obj.start >= comp_obj.end:
            break

        # if the start possition is a "." move that start comparitor one to the right
        elif comp_obj.data[comp_obj.start] != ".":
            comp_obj.move("start")
        
        # if the end position is not "." move the end comparitor left
        elif comp_obj.data[comp_obj.end] == ".":
            comp_obj.move("end")
        else:
            comp_obj.swap()

    # clear the count down
    print("          ", end="\r")

    # calculate checksum
    chum = check_sum(comp_obj.data)

    # print checksum
    print("\n ---------- Checksum:", chum, " ---------- \n")

    # print time the program took to run
    print(f" ---------- {time.time() - start_time} seconds ---------- \n")
  
# calculate check sum as defined in problem
def check_sum(data):

    # initiate chum (shecksum) counter at 0
    chum = 0
    
    # itterate throw data and add all intergers, multiplied by there posstion, to the sum
    for i in range(len(data) - 1):
        if data[i] == ".":
            return chum
        else:
            chum += int(data[i]) * i
        
# create file length data sets for full data set
def file_length(input_number):

    # create a string of length input that is the current block repeated
    global current_block
    compression = [str(current_block)] * input_number
    current_block += 1
    return compression

# create free space data set for full data set
def free_space(input_number):
    
    # return a string of "." the input number of times
    return ["."] * input_number

# toggle between file_length and free_space functions in the flip_flop function
def toggle():

    # chenge the global flip_flop variable to other function
    global flip_flop
    if flip_flop == file_length:
        flip_flop = free_space
    else:
        flip_flop = file_length

main()
