import pandas as pd

data = {
    "name": ["Rahul", "Amit", "Sara", "John", "Priya"],
    "age": [22, 19, 24, 21, 26],
    "salary": [25000, 30000, 45000, 22000, 55000],
    "city": ["Rajkot", "Surat", "Ahmedabad", "Rajkot", "Surat"]
}

df = pd.DataFrame(data)

print(df)

# Select Single Column
print(df["name"]) 

# Select Multiple Columns
print(df[["name", "salary"]])

# Select Column Subset
selected = df[["name", "city"]]

print(selected)

# Dynamic Column Selection
cols = ["name", "salary"]

print(df[cols])

# Selecting Numeric Columns Only
print(df.select_dtypes(include="number"))

# Selecting String Columns Only
print(df.select_dtypes(include="object"))
# or  Better modern version
print(df.select_dtypes(include="string"))
#or safest compatible version
print(df.select_dtypes(include=["object", "string"]))