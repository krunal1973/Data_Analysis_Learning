import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20000, 35000, 30000, 45000, 40000]

plt.plot(months, sales)

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()