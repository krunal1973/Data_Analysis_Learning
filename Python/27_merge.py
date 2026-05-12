import pandas as pd 

import pandas as pd

employee = pd.DataFrame({
    "employee_id": [1, 2, 3, 4],
    "name": ["Rahul", "Amit", "Sara", "John"],
    "department": ["HR", "IT", "Sales", "Finance"]
})

salary = pd.DataFrame({
    "employee_id": [1, 2, 3],
    "salary": [50000, 70000, 65000]
})


result = pd.merge(employee, salary, on="employee_id",how="right")
print(result)

result = pd.merge(employee, salary, on="employee_id", how="left")
print(result)

result = pd.merge(employee, salary, on="employee_id", how="outer")
print(result)

result = pd.merge(employee, salary, on="employee_id", how="inner")
print(result)

