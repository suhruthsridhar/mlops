import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Check if the table exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    department TEXT,
    cgpa REAL,
    year INTEGER
)
""")

# Count records
cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]
print("Total records:", count)

# Display records
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()