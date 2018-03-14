student = {
    'name': 'Mark',
    'age': 24,
    'gender': None
}

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


del student['item']
