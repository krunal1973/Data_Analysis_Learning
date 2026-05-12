import pandas as pd
import numpy as np

data = {
    "name": ["Rahul", "Amit", "Sara", "John"],
    "salary": [50000, np.nan, 65000, 70000],
    "city": ["Ahmedabad", "Mumbai", np.nan, "Pune"]
}

df = pd.DataFrame(data)

print(df)
print(df.isnull())
print(df.isnull().sum())