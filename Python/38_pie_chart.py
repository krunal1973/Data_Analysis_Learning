import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Furniture"]
sales = [40000, 30000, 50000]

plt.pie(sales, labels=categories)

plt.title("Category Sales Distribution")

plt.show()