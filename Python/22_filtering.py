import pandas as pd
data = {
    "name": ["Rahul", "Amit", "Sara", "John", "Priya"],
    "age": [22, 19, 24, 21, 26],
    "salary": [25000, 30000, 45000, 22000, 55000],
    "city": ["Rajkot", "Surat", "Ahmedabad", "Rajkot", "Surat"]
}
df = pd.DataFrame(data)

# Basic filtering
print(df[df["salary"]> 30000])

# multiple conditions
# And condition
print(df[(df["age"] > 20) & (df["salary"] > 30000)])
# OR condition
print(df[(df["city"] == "Rajkot") | (df["salary"] > 50000)])

# Advanced filtering
# Using isin() method   
print(df[df["city"].isin(["Rajkot", "Surat"])])
# Using str.contains() method
print(df[df["name"].str.contains("a", case=False)])
# Using between() method
print(df[df["age"].between(20, 25)])
# Using query() method
print(df.query("age > 20 and salary > 30000"))
# Null values filtering
data_with_nulls = {
    "name": ["Rahul", "Amit", "Sara", "John", "Priya"],
    "age": [22, 19, None, 21, 26],
    "salary": [25000, None, 45000, 22000, 55000],
    "city": ["Rajkot", "Surat", "Ahmedabad", None, "Surat"]
}
df_with_nulls = pd.DataFrame(data_with_nulls)
print(df_with_nulls[df_with_nulls["age"].isnull()])
print(df_with_nulls[df_with_nulls["salary"].notnull()])
print(df_with_nulls[df_with_nulls["city"].isnull()])
