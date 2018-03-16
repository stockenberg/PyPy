student = {
    'name': 'Mark',
    'age': 24,
    'gender': None
}

for key in student:
    print("Students {key} is {value}".format(key=key, value=student[key]))

for value in student.values():
    print(value)

for key in student.keys():
    print(key)

if "name" in student:
    print(True)

del student['age']

# items is a tuple - use tuple unpacking
for key, value in student.items():
    print(key)
    print(value)

students = [student]

print(students)

# Aufruf
print(student["name"])

# Keyerror
# print(student['last'])

print(student.get('last', 'Unknown'));

# all Keys
print(student.keys())

# all values
print(student.values())

# Dictionaries and Tuples
names_and_ages = [("alice", 25), ("Peter", 24)]
d = dict(names_and_ages)

new_dict = dict(test="hallo", pups="test")
# Copy
x = new_dict.copy()
f = dict(new_dict)

# update values in existing dict - if is key - value is replaced
f.update(new_dict)


del student['item']
