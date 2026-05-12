import pandas as pd

data = {
    "name": ["Rahul", "Amit", "Sara", "John", "Priya"],
    "age": [22, 19, 24, 21, 26],
    "salary": [25000, 30000, 45000, 22000, 55000],
    "city": ["Rajkot", "Surat", "Ahmedabad", "Rajkot", "Surat"]
}

df = pd.DataFrame(data)

print(df)

# Sort in Ascending order 
print(df.sort_values("salary"))

# Sort in Descending order 
print(df.sort_values("salary", ascending=False))

# Sorting by Multiple Columns
print(df.sort_values(["city", "salary"], ascending=[True, False]))

# Sorting Strings
print(df.sort_values("name"))

#Sorting with NULL Values
import numpy as np

df.loc[2, "salary"] = np.nan

print(df.sort_values("salary", na_position="first"))