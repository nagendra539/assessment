import pandas as pd

Employees = pd.read_excel("table_data.xlsx", sheet_name="Employees")
Devices = pd.read_excel("table_data.xlsx", sheet_name="Devices")
print(Employees[0])
print(Devices[0])