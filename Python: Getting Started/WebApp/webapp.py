from flask import Flask, render_template, redirect, url_for, request
from classes.student import Student

students = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        new_student = Student(name=new_student_name, student_id=new_student_id, lastname=new_student_last_name)
        students.append(new_student)

        print(students)

        return redirect(url_for("students_page"))
    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
