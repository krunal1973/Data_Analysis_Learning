import pandas as pd

data = {
    "name": ["Rahul", "Amit", "Rahul", "Sara", "Amit"],
    "city": ["Ahmedabad", "Mumbai", "Ahmedabad", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)

print(df.duplicated())

# shows only the duplicated rows
print(df[df.duplicated()])

# remove the duplicated rows
df = df.drop_duplicates()
print(df)