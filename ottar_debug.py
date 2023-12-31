from logic_layer.voyage_logic import Voyage_Logic
from logic_layer.employee_logic import Employee_Logic
from data_layer.data_wrapper import Data_Wrapper
from Model.employee import Employee
from UI_layer.input_validate import Validate


#voyage_number,dep_from,arr_at,aircraft_id,date_out,date_home,captain,copilot,flight_service_manager,flight_attendant1,flight_attendant2

data_class = Data_Wrapper()
e = Employee

'''
e.voyage_number = input("voyage_number ")
e.dep_from = input("dep_from ")
e.arr_at = input("arr_at ")
e.aircraft_id = input("aircraft_id ")
e.date_out = input("date_out ")
e.date_home = input("date_home ")
e.captain = input("captain  ")
e.copilot = input("copilot ")
e.flight_service_manager = input("flight_service_manager ")
e.flight_attendant1 = input("flight_attendant1  ")
e.flight_attendant2 = input("flight_attendant2  ")
'''
'''
'''
date = input("date ")

logic_class = Voyage_Logic(data_class)
result = logic_class.check_day(date)

print(result[0])

aircraft_id = input("Enter aircraft ID: ")
validate_instance = Validate()  # Create an instance of the Validate class
result = validate_instance.validate_cap(aircraft_id)  # Call the method on the instance

print("Validation result:", result)