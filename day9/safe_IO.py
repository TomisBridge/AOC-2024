"""     except ValueError:
        print("\n ---------- please input file type .txt ---------- \n")
        """
 
def safe_get(target):

    data = None
    try:
        data = format_target(target)
    except FileNotFoundError:
        print("\n ---------- please input file name from the same folder as this program ---------- \n")
    else:
        return data


def format_target(target_file):

    # import data
    my_file = open(target_file, "r")
    data = my_file.read()

    # split into sublists and eliminate empty lists
    int_list = []
    for item in data:
        if item != "\n": # eliminate empty lists
            int_list.append(int(item))

    return int_list

