students = []


class Student:

    # are also statics (class attribute)
    name = None
    student_id = None
    school_name = "Springfield Elementary"

    def __init__(self, name: str, student_id=332):
        self.name = name
        self.student_id = student_id
        # instance attribute
        self.noclassattribute = "test"
        self.add_student(name.title(), student_id)

    def add_student(self, name, student_id=332):
        student = {'name': name, 'student_id': student_id}
        students.append(student)

    # no memory reference - instead string name
    def __str__(self):
        return "StudentClass " + self.name

    def get_school_name(self):
        print(self.school_name)

#student = Student("marten")

print(students)
#print(student)