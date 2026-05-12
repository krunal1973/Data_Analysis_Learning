import pandas as pd

df = pd.read_csv("sample_sales.csv")

print(df.head())

print(df.info())

df = pd.read_excel("sample_sales.xlsx")

print(df.head())

print(df.info())