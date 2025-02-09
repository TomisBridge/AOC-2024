import sys
import time
from safe_IO import safe_get
from compressor import data_string

start_time = time.time()

def main():

    data = safe_get(sys.argv[1])

    global current_block
    current_block = 0
    global flip_flop
    flip_flop = file_length
    uncompressed = ""

    for number in data:
        uncompressed += flip_flop(number)
        toggle()

    comp_obj = data_string(uncompressed, 0, len(uncompressed) - 1)
    print(comp_obj.string)

    while True:
        if comp_obj.start >= comp_obj.end:
            break
        elif comp_obj.string[comp_obj.start] != ".":
            comp_obj.move("start")
        elif comp_obj.string[comp_obj.end] == ".":
            comp_obj.move("end")
        else:
            comp_obj.swap()

    print(comp_obj.string)
    chum = check_sum(comp_obj.string)
    print(chum)
    print(f" ----- {time.time() - start_time} seconds ----- ")
  
def check_sum(string):
    chum = 0
    for i in range(len(string) - 1):
        if string[i] == ".":
            return chum
        else:
            chum += int(string[i]) * i
        
def file_length(input_number):
    global current_block
    compression = str(current_block) * input_number
    current_block += 1
    return compression

def free_space(input_number):
    return "." * input_number

def toggle():
    global flip_flop
    if flip_flop == file_length:
        flip_flop = free_space
    else:
        flip_flop = file_length

main()
