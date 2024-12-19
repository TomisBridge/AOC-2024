import re

def main():
    
    data = format_AOC_day3(input("input name: "))
    print(data)

    allow_char = "mul()0123456789,"

    allow_data = ""
    for char in data:
        if char in allow_char:
            allow_data += char

    print(allow_data)

    allow_char_list = allow_data.replace("m", " m").split(" ")

    print(allow_char_list)

    filtered = []
    for item in allow_char_list:
        if re.match(item, r"mul(2,4)"):
            filtered.append(item)

    print(filtered)
def format_AOC_day3(target_file):

    #import data and store it in data as a str
    my_file = open(target_file, "r")
    data = []
    data = my_file.read()


    # close file
    my_file.close()
    
    return data

main()
