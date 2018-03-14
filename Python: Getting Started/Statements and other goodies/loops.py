names = ["Martne", "Test", "einszweidrei"]

for x in names:
    print(x)
    print("The students name is {0}".format(x))

for x in range(len(names)):
    print(x)
    print(names[x])

# Error - names is an list
# print(range(names))
print(range(len(names)))

print(range(5, 10))  # [5, 6, 7, 8, 9]
print(range(5, 10, 2))  # [5, 7, 9]
