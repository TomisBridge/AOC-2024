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

       
    pass_list = []
    for update in updates:
        if if_used(rules, update):
            pass_list.append(update[int(len(update)/2)])
    print(sum(pass_list))

def if_used(rules, update):
    update_str = " ".join(map(str, update))
    for rule in rules:
        pattern = f".*{rule[1]}.*{rule[0]}.*"
        if re.match(pattern, update_str):
            return False
    return True


main()
