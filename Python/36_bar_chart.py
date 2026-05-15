import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Keyboard", "Mouse"]
sales = [50000, 70000, 30000, 20000]

plt.bar(products, sales)

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()