import sys
import time
from safe_IO import safe_get
from compressor2 import data_list

start_time = time.time()

def main():
    sys.setrecursionlimit(1000000000)

    data = safe_get(sys.argv[1])

    global current_block
    current_block = 0
    global flip_flop
    flip_flop = file_length
    ncompressed = []

    for number in data:
        ncompressed.append(flip_flop(number))
        toggle()

    uncompressed = []
    for u in ncompressed:
        if u != []:
            uncompressed.append(u)

    comp_obj = data_list(uncompressed, 0, len(uncompressed) - 1)

    for i in range(1, 50):
        print(comp_obj.data[i])

    for i in range(1, 50):
        print(comp_obj.data[len(comp_obj.data) - i])


    while comp_obj.end > 0:
        print(comp_obj.at(comp_obj.start), comp_obj.at(comp_obj.end))
        if comp_obj.end % 10 == 0:
            print(comp_obj.end, end="\r")
        if comp_obj.at(comp_obj.end)[0] != ".":
            push_back(comp_obj)
            comp_obj.mel()
        else:
            comp_obj.mel()

    compressed = []
    for item in comp_obj.data:
        compressed += item

    chum = check_sum(compressed)
    print("")
    print(chum)

    print(f" ----- {time.time() - start_time} seconds ----- ")
  
def push_back(obj):
    print("\n start: ", obj.start, "\n end: ", obj.end, "\n ", obj.at(obj.start))
    
    if obj.start >= obj.end:
        #print(obj.data, "\n start: ", obj.start, "\n end: ", obj.end, "\n 1")
        obj.start = 0

    elif obj.at(obj.start)[0] != ".":
        #print(obj.data, "\n start: ", obj.start, "\n end: ", obj.end, "\n 2")
        obj.msr()
        push_back(obj)
    
    elif len(obj.at(obj.start)) > len(obj.at(obj.end)): 
        #print(obj.data, "\n start: ", obj.start, "\n end: ", obj.end, "\n 3")
        obj.breakup()
        obj.mer()
        obj.swap()
        obj.start = 0

    elif len(obj.at(obj.start)) == len(obj.at(obj.end)):
        #print(obj.data, "\n start: ", obj.start, "\n end: ", obj.end, "\n 4")
        obj.swap()
        obj.start = 0

    elif len(obj.at(obj.start)) < len(obj.at(obj.end)):
        #print(obj.data, "\n start: ", obj.start, "\n end: ", obj.end, "\n 5")
        obj.msr()
        push_back(obj)

def check_sum(data):
    chum = 0
    for i in range(len(data) - 1):
        if data[i] != ".":
            chum += int(data[i]) * i
    return chum
        
def file_length(input_number):
    global current_block
    compression = []
    for _ in range(input_number):
        compression.append(str(current_block))
    current_block += 1
    return compression

def free_space(input_number):
    compression = []
    for _ in range(input_number):
        compression += "."
    return compression

def toggle():
    global flip_flop
    if flip_flop == file_length:
        flip_flop = free_space
    else:
        flip_flop = file_length

main()
