import pandas as pd

data = {
    "name": ["Rahul", "Amit", "Sara", "John", "Priya", "Karan"],

    "department": [
        "IT",
        "HR",
        "IT",
        "Sales",
        "HR",
        "IT"
    ],

    "salary": [
        50000,
        40000,
        70000,
        45000,
        42000,
        65000
    ]
}

df = pd.DataFrame(data)
print(df)

group_data = df.groupby("department")["salary"].sum()
print(group_data)

avg_salary = df.groupby("department")["salary"].mean()
print(avg_salary)

max_salary = df.groupby("department")["salary"].max()
print(max_salary)

employee_count = df.groupby("department")["name"].count()
print(employee_count)

result = df.groupby("department")["salary"].agg(
    ["sum", "mean", "max", "min", "count"]
)
print(result)