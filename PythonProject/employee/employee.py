# employee.py

import pandas as pd


employee_data = {

    "Employee_ID": [101,102,103,104,105,106],

    "Employee_Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Sneha",
        "Kiran",
        "Anjali"
    ],

    "Department": [
        "AI",
        "AI",
        "Data Science",
        "Data Science",
        "Python",
        "Python"
    ],

    "Salary": [
        50000,
        55000,
        60000,
        58000,
        45000,
        48000
    ],

    "Mentor_Capacity": [
        30,
        35,
        40,
        35,
        25,
        30
    ]
}


# Convert dictionary to DataFrame

employee_df = pd.DataFrame(employee_data)


print("Employee Data")
print(employee_df)


# Save employee data

employee_df.to_csv(
    "Employee_Data.csv",
    index=False
)

print("\nEmployee data saved successfully")