import pandas as pd

df1 = pd.DataFrame({
    "name": ["Rahul", "Amit"]
})

df2 = pd.DataFrame({
    "name": ["Sara", "John"]
})

result = pd.concat([df1, df2],ignore_index=True)
print(result)

df1 = pd.DataFrame({
    "name": ["Rahul", "Amit"]
})

df2 = pd.DataFrame({
    "marks": [85, 90]
})

result1 = pd.concat([df1, df2], axis=1)
print(result1)