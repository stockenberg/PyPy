
mylist = ["Marten", "test", "3", 5]
print(mylist)

print(mylist[2])

# get the Last element
print(mylist[-1])


mylist[1] = "Pups"
print(mylist[1])

mylist.insert(2, "value")
mylist.append('Test')
mylist.count("some_val")  # returns number of same values

if "val" in ["my", "val", "is", "test"]:
    print("this is true")

if "val" not in ["my", "val", "is", "test"]:
    print(False)

# Check if Entry is in List
print("Test" in mylist)

print(len(mylist))

# Delete Item in List, items shifts and get new indizes
del mylist[2]
del mylist[mylist.index("Wert der gelöscht werden soll")]

my_new_list = [-1, +1] * 5


print(my_new_list)

#Slicing
print(mylist)

newList = mylist[:]
newList = mylist.copy()
newList = list(mylist)

# Ignore first element
print(mylist[1:])

# Ignore first an last Element in list
print(mylist[1:-1])

'''reverse / sorting '''

mylist.reverse()
h = "this is my long sentance".split()
h.sort(key=len)
h = sorted(h)
h = reversed(h)

word_list = ["Hallo", "du", "Dude"]
lengths = []
# List Comprehension
[len(word) for word in word_list]
# [expr(item) for item in iterable]
''' ist das selbe wie: '''
for word in word_list:
    lengths.append(len(word))
