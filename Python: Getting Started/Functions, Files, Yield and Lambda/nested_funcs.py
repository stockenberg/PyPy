
def get_students():
    students = ["peter", "hans", "marten"]

    def get_students_titlecase():  #python closure
        students_titlecase = []
        ## has access to variables in the outer functions
        for student in students:
            students_titlecase.append(student.title())
        return students_titlecase
    students_titlecase_names = get_students_titlecase()
    print(students_titlecase_names)


get_students()