import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 60, 65, 75, 85, 95]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()