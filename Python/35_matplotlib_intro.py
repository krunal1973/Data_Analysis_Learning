import pandas as pd
import matplotlib.pyplot as plt

data = {
    "category": ["Electronics", "Fashion", "Accessories"],
    "sales": [90000, 8000, 8200]
}

df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(8,5))
plt.bar(df["category"], df["sales"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Bar chart with different colors
plt.figure(figsize=(8,5))
plt.bar(df["category"], df["sales"], color="green")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# line chart
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [10000, 15000, 12000, 18000, 22000]

plt.figure(figsize=(8,5))
plt.plot(months, sales, marker="o", linestyle="--", color="orange")
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# Pie chart
categories = ["Electronics", "Fashion", "Accessories"]
sales = [90000, 8000, 8200]
plt.figure(figsize=(6,6))
plt.pie(sales, labels=categories)
plt.title("Sales Distribution")
plt.show()