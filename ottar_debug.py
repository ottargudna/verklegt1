from logic_layer.voyage_logic import Voyage_Logic
from logic_layer.employee_logic import Employee_Logic
from data_layer.data_wrapper import Data_Wrapper
from Model.employee import Employee


#nid,name,role,rank,licence,address,phone_nr,email,homephone_nr
data_class = Data_Wrapper()
e = Employee
e.nid = input("enter NID: ")

e.role = input("role ")
e.rank = input("rank ")
e.licence = input("licence ")
e.address = input("addres ")
e.phone_nr = input("phone number ")
e.email = input("email ")
e.homephone_nr = input("homephone nr ")

logic_class = Employee_Logic(data_class)
result = logic_class.edit_employee(e)

print(result)

