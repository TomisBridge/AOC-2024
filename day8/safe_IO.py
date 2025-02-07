
def safe_get(target):

    data = None
    try:
        data = format_target(target)
    except ValueError:
        print("\n ---------- please input file type .txt ---------- \n")
    except FileNotFoundError:
        print("\n ---------- please input file name from the same folder as this program ---------- \n")
    else:
        return data


def format_target(target_file):

    # import data
    my_file = open(target_file, "r")
    data = my_file.read()

    # split into list at \n
    data_list = data.split("\n")

    # split into sublists and eliminate empty lists
    data_lists = []
    for item in data_list:
        if item != "": # eliminate empty lists
            data_lists.append(item.replace(":", "").split(" "))

    # convert list items into interger
    int_lists = []
    for items in data_lists:
        int_lists.append(list(map(int, items)))
        
    return int_lists

