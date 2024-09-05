import pandas as pd

Employees = pd.read_excel("table_data.xlsx", sheet_name="Employees")
Devices = pd.read_excel("table_data.xlsx", sheet_name="Devices")
common1 = []

# we are comparing the employee_id and id colums in two sheets and append the id to the list 
for id in Employees['id']:
    for empid in Devices['employee_id']:
        if id == empid:
            common1.append(id)

# gettting the data which ids are not present ih the list.
Difference_list= Employees[~Employees['id'].isin(common1)]

print("Employee names which are not using the Company device:")
# print the firstname and last names of the employees who are not using the company device.
print (Difference_list[['first_name','last_name']].values)
