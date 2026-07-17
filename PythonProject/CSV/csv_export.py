import subprocess
import sys

while True:
    print("\n===== Management System =====")
    print("1. Employee Management")
    print("2. Student Management")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subprocess.run([sys.executable, "employee.py"])

    elif choice == "2":
        subprocess.run([sys.executable, "fstudent.py"])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")