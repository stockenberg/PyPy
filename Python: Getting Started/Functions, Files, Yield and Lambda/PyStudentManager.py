students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())  # like ucfirst
    return students_titlecase


def print_students():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=1):
    student = {'name': name, 'student_id': student_id}
    students.append(student)


def save_file(student):
    try:
        f = open('students.txt', "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Cant save")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Couldn read")


read_file()
print_students()

while True:
    prompt = input("Do you want to stop? ")
    if prompt == "yes":
        break

    student_name = input("Enter a student name: ")
    student_id = input("Enter an Student id: ")

    save_file(student_name)
    print(students)


