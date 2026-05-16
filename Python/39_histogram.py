import matplotlib.pyplot as plt

sales = [100, 120, 150, 180, 200, 220, 250, 250, 280, 300,
         320, 350, 400, 420, 450, 500]

plt.hist(sales)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()