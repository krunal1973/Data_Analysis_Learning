import pandas as pd

data = {
    "name": [" Rahul ", "AMIT", "sara", "John  "]
}

df = pd.DataFrame(data)
print(df)

# remove extra spaces
df["name"] = df["name"].str.strip()
print(df)

# convert to lowercase
df["name"] = df["name"].str.lower()
print(df)

# convert to uppercase
df["name"] = df["name"].str.upper()
print(df)

# Capitalize Properly
df["name"] = df["name"].str.title()
print(df)