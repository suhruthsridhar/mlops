import sqlite3

# ==========================================
# Create Student Database
# ==========================================
student_conn = sqlite3.connect("student.db")
student_cursor = student_conn.cursor()

student_cursor.execute("""
DROP TABLE IF EXISTS students
""")

student_cursor.execute("""
CREATE TABLE students(
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    department TEXT,
    cgpa REAL,
    year INTEGER
)
""")

student_conn.commit()

print("Student table created successfully.")

student_conn.close()


# ==========================================
# Create Employee Database
# ==========================================
employee_conn = sqlite3.connect("employee.db")
employee_cursor = employee_conn.cursor()

employee_cursor.execute("""
DROP TABLE IF EXISTS employees
""")

employee_cursor.execute("""
CREATE TABLE employees(
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    department TEXT,
    salary INTEGER,
    experience INTEGER
)
""")

employee_conn.commit()

print("Employee table created successfully.")

employee_conn.close()

print("\nDatabase setup completed successfully.")