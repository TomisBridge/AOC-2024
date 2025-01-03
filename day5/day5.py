def main():
    
    # import data from user specified file
    rules = safe_get("rules: ", format_rules)
    if rules == None:
        print("\n --------- program ended ---------- \n")
        return

    # import updates from user specified file
    updates = safe_get("updates: ", format_updates)
    if updates == None:
        print("\n --------- program ended ---------- \n")
        return

    print(rules)
    print(updates)

def safe_get(prompt, func):

    data = None
    while True:
        try:
            target_rules = input(prompt)
            if target_rules != "q":
                data = func(target_rules)
        except ValueError:
            print("\n  ---------- please input file type .txt or type ---------- \
                  \n ---------- or type q to quit ---------- \n")
        except FileNotFoundError:
            print("\n ---------- please input file name from the same folder as this program ----------\
                  \n ---------- or type q to quit ---------- \n")
        except:
            print("\n ---------- Unkown error ----------- \
                  \n ---------- or type q to quit ---------- \n")
        else:
            return data


def format_rules(target_file):

    # import data and split at \n and | to create a list of lists
    my_file = open(target_file, "r")
    data = my_file.read()

    # split into list at \n
    data_list = data.split("\n")

    # split into sublists at | 
    data_lists = []
    for item in data_list:
        if item != "": # eliminate empty lists
            data_lists.append(item.split("|"))

    int_lists = []
    for items in data_lists:
         int_lists.append(list(map(int, items)))

    # return list of lists
    return int_lists

def format_updates(target_file):

    # import data and split at \n and ,
    my_file = open(target_file, "r")
    data = my_file.read()

    # split into list at \n
    data_list = data.split("\n")

    # split into sublists at , 
    data_lists = []
    for item in data_list:
        if item != "": # eliminate empty lists
            data_lists.append(item.split(","))

    # convert all items of sub lists into intergers
    int_lists = []
    for items in data_lists:
         int_lists.append(list(map(int, items)))

    return int_lists

  

main()
