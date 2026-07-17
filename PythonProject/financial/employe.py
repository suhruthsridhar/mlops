import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")


def setup_database(conn):
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute("DROP TABLE IF EXISTS employees")

    # Employees table
    cursor.execute("""
        CREATE TABLE employees(
                                  employee_id     TEXT PRIMARY KEY,
                                  department      TEXT,
                                  salary          REAL,
                                  mentor_capacity INTEGER
        )
    """)

    # Students table
    cursor.execute("""
        CREATE TABLE students(
            student_id TEXT PRIMARY KEY,
            department TEXT,
            course TEXT,
            fee REAL
        )
    """)

    employees = [
        ('EMP001', 'Data Science', 85000, 25),
        ('EMP002', 'Data Science', 90000, 30),
        ('EMP003', 'Data Science', 60000, 20),

        ('EMP004', 'Web Development', 70000, 40),
        ('EMP005', 'Web Development', 75000, 45),

        ('EMP006', 'UX/UI Design', 68000, 25),
        ('EMP007', 'UX/UI Design', 72000, 25),

        ('EMP008', 'Cyber Security', 80000, 20),
        ('EMP009', 'Cyber Security', 62000, 15),

        ('EMP010', 'Marketing', 50000, 50)
    ]

    cursor.executemany(
        "INSERT INTO employees VALUES (?,?,?,?)",
        employees
    )

    students = []

    # Data Science = 80 students
    students += [
        (f'STU_DS_{i}', 'Data Science', 'AI & Machine Learning', 4000)
        for i in range(1, 81)
    ]

    # Web Development = 70 students
    students += [
        (f'STU_WD_{i}', 'Web Development', 'Full-Stack Dev', 3000)
        for i in range(1, 71)
    ]

    # UX/UI = 40 students
    students += [
        (f'STU_UX_{i}', 'UX/UI Design', 'Product Design', 3500)
        for i in range(1, 41)
    ]

    # Cyber Security = 45 students
    students += [
        (f'STU_CY_{i}', 'Cyber Security', 'Ethical Hacking', 4500)
        for i in range(1, 46)
    ]

    # Marketing = 30 students
    students += [
        (f'STU_MK_{i}', 'Marketing', 'Digital Marketing', 2000)
        for i in range(1, 31)
    ]

    cursor.executemany(
        "INSERT INTO students VALUES (?,?,?,?)",
        students
    )

    conn.commit()


def run_analysis(conn):

    sql = """
    SELECT
        s.department AS Department,
        COUNT(DISTINCT s.student_id) AS Total_Students,
        COUNT(DISTINCT e.employee_id) AS Current_Mentors,
        SUM(DISTINCT e.mentor_capacity) AS Total_Capacity,
        SUM(s.fee) AS Total_Revenue,
        SUM(DISTINCT e.salary) AS Total_Cost,
        SUM(s.fee)-SUM(DISTINCT e.salary) AS Profit_Loss,
        ROUND(
            COUNT(DISTINCT s.student_id)*100.0/
            SUM(DISTINCT e.mentor_capacity),2
        ) AS Capacity_Utilization_Pct
    FROM students s
    LEFT JOIN employees e
        ON s.department=e.department
    GROUP BY s.department
    """

    df = pd.read_sql_query(sql, conn)

    # ---------------------------------------
    # Balance students between departments
    # ---------------------------------------

    df["Balanced_Students"] = df["Total_Students"]

    transfers = []

    overloaded = []
    underloaded = []

    for idx, row in df.iterrows():

        difference = row["Total_Students"] - row["Total_Capacity"]

        if difference > 0:

            overloaded.append({
                "index": idx,
                "dept": row["Department"],
                "excess": difference
            })

        elif difference < 0:

            underloaded.append({
                "index": idx,
                "dept": row["Department"],
                "space": -difference
            })

    for over in overloaded:

        excess = over["excess"]

        for under in underloaded:

            if excess == 0:
                break

            if under["space"] == 0:
                continue

            moved = min(excess, under["space"])

            df.loc[over["index"], "Balanced_Students"] -= moved
            df.loc[under["index"], "Balanced_Students"] += moved

            transfers.append(
                f"{moved} students moved from "
                f"{over['dept']} -> {under['dept']}"
            )

            excess -= moved
            under["space"] -= moved

    df["Balanced_Utilization_%"] = round(
        df["Balanced_Students"] /
        df["Total_Capacity"] * 100,
        2
    )

    def suggestion(row):

        if row["Balanced_Utilization_%"] > 100:
            return "Still Over Capacity"

        elif row["Balanced_Utilization_%"] == 100:
            return "Balanced"

        else:
            return "Capacity Available"

    df["Suggestion"] = df.apply(suggestion, axis=1)

    return df, transfers


def plot_results(df):

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # ------------------------
    # Profit chart
    # ------------------------

    sns.barplot(
        x="Profit_Loss",
        y="Department",
        data=df,
        palette="RdYlGn",
        ax=axes[0]
    )

    axes[0].set_title("Department-wise Net Profit / Loss ($)")
    axes[0].set_xlabel("Profit / Loss ($)")

    for container in axes[0].containers:
        axes[0].bar_label(
            container,
            fmt="$%.0f",
            padding=3
        )

    # ------------------------
    # Balanced utilization
    # ------------------------

    sns.barplot(
        x="Balanced_Utilization_%",
        y="Department",
        data=df,
        palette="Blues_r",
        ax=axes[1]
    )

    axes[1].axvline(
        100,
        color="red",
        linestyle="--",
        linewidth=2,
        label="100% Capacity"
    )

    axes[1].set_title("Capacity Utilization After Balancing")
    axes[1].set_xlabel("Utilization %")

    axes[1].legend()

    for container in axes[1].containers:

        labels = [
            f"{v:.1f}%"
            for v in df["Balanced_Utilization_%"]
        ]

        axes[1].bar_label(
            container,
            labels=labels,
            padding=3
        )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    connection = sqlite3.connect(":memory:")

    setup_database(connection)

    results, transfers = run_analysis(connection)

    print("\n================ ORIGINAL & BALANCED RESULTS ================\n")
    print(results.to_string(index=False))

    print("\n================ STUDENT TRANSFERS ================\n")

    if transfers:
        for t in transfers:
            print(t)
    else:
        print("No transfers required.")

    print("\n===================================================\n")

    plot_results(results)

    connection.close()