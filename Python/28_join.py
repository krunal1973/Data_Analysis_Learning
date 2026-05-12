import pandas as pd

students = pd.DataFrame({
    "name": ["Rahul", "Amit", "Sara","John"]
}, index=[1, 2, 3,4])

marks = pd.DataFrame({
    "marks": [85, 90, 88]
}, index=[1, 2, 3])


result = students.join(marks, how="left")
print(result)
result = students.join(marks, how="right")
print(result)
result = students.join(marks, how="outer")
print(result)
result = students.join(marks, how="inner")
print(result)
# default join 
result=students.join(marks)
print(result)