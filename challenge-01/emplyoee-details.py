import pandas as pd

Employees = pd.read_excel("table_data.xlsx", sheet_name="Employees")
Devices = pd.read_excel("table_data.xlsx", sheet_name="Devices")
print(Employees)
print(Devices)
common1 = []

for id in Employees['id']:
    for empid in Devices['employee_id']:
        if id == empid:
            common1.append(id)

print(common1)

filtered_df = Employees[Employees['id'].isin(common1)]

print(filtered_df.['first_name'])


            
            
        


