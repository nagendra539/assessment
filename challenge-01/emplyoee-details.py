import pandas as pd

Employees = pd.read_excel("table_data.xlsx", sheet_name="Employees")
Devices = pd.read_excel("table_data.xlsx", sheet_name="Devices")
print(Employees)
print(Devices)

Emp_Dev = pd.merge(Employees, Devices, on='employee_id', how=left, indicator=True)

print(Emp_Dev)