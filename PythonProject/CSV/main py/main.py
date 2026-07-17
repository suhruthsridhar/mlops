class Employee:
    employees = {}

    @classmethod
    def create(cls, emp_id, name, department):
        if emp_id in cls.employees:
            return f"Employee ID {emp_id} already exists."

        cls.employees[emp_id] = {
            "Name": name,
            "Department": department
        }
        return f"Employee '{name}' added successfully."

    @classmethod
    def read(cls):
        if not cls.employees:
            return "No employee records found."

        print("\nEmployee Records")
        print("-" * 40)

        for emp_id, details in cls.employees.items():
            print(f"Employee ID : {emp_id}")
            print(f"Name        : {details['Name']}")
            print(f"Department  : {details['Department']}")
            print("-" * 40)

    @classmethod
    def update(cls, emp_id, name, department):
        if emp_id not in cls.employees:
            return f"Employee ID {emp_id} not found."

        cls.employees[emp_id]["Name"] = name
        cls.employees[emp_id]["Department"] = department

        return f"Employee ID {emp_id} updated successfully."

    @classmethod
    def delete(cls, emp_id):
        if emp_id not in cls.employees:
            return f"Employee ID {emp_id} not found."

        removed = cls.employees.pop(emp_id)
        return f"Employee '{removed['Name']}' deleted successfully."


# Main Menu
while True:
    print("\n===== Employee Management System =====")
    print("1. Create Employee")
    print("2. Read Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")

        print(Employee.create(emp_id, name, department))
