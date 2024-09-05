import pandas as pd

Employees = pd.read_excel("table_data.xlsx", sheet_name="Employees")
Devices = pd.read_excel("table_data.xlsx", sheet_name="Devices")
print(Employees)
print(Devices)

for id in Employees['id']:
    for empid in Devices['employee_id']:
        if id != empid:
            print(id)
        


