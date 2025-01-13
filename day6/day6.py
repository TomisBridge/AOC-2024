from safe_IO import safe_get
import sys

def main():
    data = safe_get(sys.argv[1])
    print(data)




main()
