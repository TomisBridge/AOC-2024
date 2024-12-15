test = list(range(10))
print(test)

print(test[3])
test.remove(test[3])
print(test)

a = ["a", "b", "c"]
a.remove("b")
print(a)

original = list(range(10))
modified = []
modified = list(original)
print(original, modified)

modified.append(4)
print(original, modified)

map(+ 1, modified)
print(original, modified)
