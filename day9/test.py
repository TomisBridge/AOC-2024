a = ["..", "."]
b = ["aaa", "bb", "cccc"]

def f(a, b):
    for i in range(len(a)):
        b.append(a[i])

f(a, b)

print(b)
