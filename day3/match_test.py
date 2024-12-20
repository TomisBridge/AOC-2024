import re

string = input("input string: ")
pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)" 
spattern = r"[0-9]{1,3}"

result = re.findall(spattern, string)

print(result)


