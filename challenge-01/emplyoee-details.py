import pandas as pd

Employees = pd.read_excel("table_data.xlsx", sheet_name="Employees")
Devices = pd.read_excel("table_data.xlsx", sheet_name="Devices")
common1 = []

for id in Employees['id']:
    for empid in Devices['employee_id']:
        if id == empid:
            common1.append(id)
print("Employee names which are not using the Company device:")
Difference_list= Employees[~Employees['id'].isin(common1)]

print (Difference_list['first_name'] : Difference_list['last_name'])