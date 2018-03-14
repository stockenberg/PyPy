
mylist = ["Marten", "test", "3", 5]
print(mylist)

print(mylist[2])

# get the Last element
print(mylist[-1])


mylist[1] = "Pups"
print(mylist[1])

mylist.append('Test')


# Check if Entry is in List
print("Test" in mylist)

print(len(mylist))

# Delete Item in List, items shifts and get new indizes
del mylist[2]

#Slicing
print(mylist)

# Ignore first element
print(mylist[1:])

# Ignore first an last Element in list
print(mylist[1:-1])

