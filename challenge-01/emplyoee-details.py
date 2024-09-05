import pandas as pd

Employees = pd.read_excel("table_data.xlsx", sheet_name="Employees")
Devices = pd.read_excel("table_data.xlsx", sheet_name="Devices")
print(Employees.index[0])
print(Devices.index[0])

for row in Employees:
    print(row[1], row[2], row[3])
