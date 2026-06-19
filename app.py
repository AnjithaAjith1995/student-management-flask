from flask import Flask, render_template, request, redirect, session
from services.student_service import load_students, add_student, delete_student, update_student

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")

    students = load_students()
    return render_template("home.html", students=students)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin":
            session["user"] = username
            return redirect("/")
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    age = request.form["age"]

    add_student(name, age)
    return redirect("/")

@app.route("/delete/<int:student_id>")
def delete(student_id):
    delete_student(student_id)
    return redirect("/")

@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit(student_id):
    students = load_students()

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]

        update_student(student_id, name, age)
        return redirect("/")

    student = next((s for s in students if s["id"] == student_id), None)

    return render_template("edit.html", student=student)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)