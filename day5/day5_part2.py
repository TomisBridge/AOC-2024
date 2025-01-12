import sys
import safe_IO
import re


def main():

    # import data from user specified file
    rules = safe_IO.safe_get("rules: ", safe_IO.format_rules)
    if rules == "q":
        sys.exit("\n ---------- Program ended ---------- \n")

    # import updates from user specified file
    updates = safe_IO.safe_get("updates: ", safe_IO.format_updates)
    if rules == "q":
        sys.exit("\n ---------- Program ended ---------- \n")

    # itterate all rules through all list. if update modified append to end of list and replace with []

    # set variable
    fail_list = updates
    list_len = len(updates)
    counter = 0
    change = 0

    # itterate through updates
    for update in fail_list:
        counter += 1
        change = 0

        # itterate through rules
        for rule in rules:

            # if the update failes the rule swap the two items and append to end of list
            if if_used(rule, update):
                fail_list[fail_list.index(update)] = [0]
                fail_list.append(swap(rule, update))
                change += 1

        # if there are been not modification done to the update then replace it with []
        if counter <= list_len and change == 0:
            fail_list[fail_list.index(update)] = [0]

    # create a list of the middle number of all list items
    pass_list = []
    for update in fail_list:
        pass_list.append(update[int(len(update) / 2)])

    # print the sum of the pass_list items
    print(sum(pass_list))


# check if the update fails the rule
def if_used(rule, update):
    update_str = " ".join(map(str, update))
    pattern = f".*{rule[1]}.*{rule[0]}.*"
    if re.match(pattern, update_str):
        return True
    return False


# swap the two impropperly ordered update entries
def swap(rule, update):
    update[update.index(rule[0])], update[update.index(rule[1])] = (
        update[update.index(rule[1])],
        update[update.index(rule[0])],
    )
    return update


main()
