from logic_layer.voyage_logic import Voyage_Logic
from logic_layer.employee_logic import Employee_Logic
from data_layer.data_wrapper import Data_Wrapper

data_class = Data_Wrapper()
nid = input("enter NID: ")
check_date = input("enter date: ")
logic_class = Employee_Logic(data_class)
result = logic_class.get_week_work(nid, check_date)

print(result)

