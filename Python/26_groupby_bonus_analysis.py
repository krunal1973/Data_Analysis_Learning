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

df["bonus"] = df["salary"] * 0.10
print(df)

bonus_summary = df.groupby("department")["bonus"].sum()
print(bonus_summary)

bonus_analysis = df.groupby("department")["bonus"].agg(
    ["sum", "mean", "max", "min"]
)
print(bonus_analysis)