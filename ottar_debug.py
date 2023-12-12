from logic_layer.voyage_logic import Voyage_Logic
from data_layer.data_wrapper import Data_Wrapper

data_class = Data_Wrapper()
check_date = input("enter date: ")
logic_class = Voyage_Logic(data_class)
working_not_working = logic_class.check_working_status_day(check_date)

print(working_not_working[0])


