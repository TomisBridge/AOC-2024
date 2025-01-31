import sys

def safe_get(target):

    data = None
    try:
        data = format_target(target)
    except ValueError:
        print("\n ---------- please input file type .txt ---------- \n")
    except FileNotFoundError:
        print("\n ---------- please input file name from the same folder as this program ----------\n")
    except:
        print("\n ---------- Unkown error ----------- \n")
    else:
        return data


def format_target(target_file):

    # import data and split at \n and | to create a list of lists
    my_file = open(target_file, "r")
    data = my_file.read()

    # split into list at \n
    data_list = data.split("\n")

    # split into sublists at | 
    data_lists = []
    for item in data_list:
        if item != "": # eliminate empty lists
            data_lists.append(item)

    # return list of lists
    return data_lists

