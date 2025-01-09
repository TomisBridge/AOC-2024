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

       
    print(rules)
    print(updates)

def if_used(rule, update):


main()
