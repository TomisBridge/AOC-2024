def main():
    
    data = format_AOC_day3(input("input name: "))
    print(data)

    allow_char = "mul()0123456789,"

    allow_data = ""
    for char in data:
        if char in allow_char:
            allow_data += char

    print(allow_data)

    allow_char_list = allow_data.split(")"e)

    print(allow_char_list)
def format_AOC_day3(target_file):

    #import data and store it in data as a str
    my_file = open(target_file, "r")
    data = []
    data = my_file.read()

    # close file
    my_file.close()
    
    return data

main()
