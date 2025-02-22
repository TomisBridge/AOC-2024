from compressor2 import data_list

a = [['.'], ['.', '.', '.'], ['1', '1', '1'], ['.', '.', '.'], ['2'], ['.', '.', '.'], ['3', '3', '3'], ['.'], ['4', '4'], ['.'], ['5', '5', '5', '5'], ['.'], ['6', '6', '6', '6'], ['.'], ['7', '7', '7'], ['.'], ['8', '8', '8', '8'], ['9']]

obj = data_list(a, 0, len(a) - 1)

while True:

    print(obj.data, "\n start: ", obj.start, "\n end: ", obj.end)
    imp = input("command: ")

    if imp == "q":
        break

    elif imp == "mel":
        obj.mel()

    elif imp == "mer":
        obj.mer()

    elif imp == "msl":
        obj.msl()

    elif imp == "msr":
        obj.msr()

    elif imp == "break":
        obj.breakup()

    elif imp == "swap":
        obj.swap()
