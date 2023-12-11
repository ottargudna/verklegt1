
from data_layer.Employee_Data import Employee_Data

data_class = Employee_Data()
result = data_class.get_all_employees()
for elem in result:
    print(elem.name + " - " + elem.nid)