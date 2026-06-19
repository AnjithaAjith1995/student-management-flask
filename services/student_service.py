import sqlite3

DB_NAME = "students.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def load_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()
    return students

def add_student(name, age):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        (name, age)
    )

    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))

    conn.commit()
    conn.close()

def update_student(student_id, name, age):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name = ?, age = ? WHERE id = ?",
        (name, age, student_id)
    )

    conn.commit()
    conn.close()