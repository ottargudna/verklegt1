
from Model.employee import Employee
from data_layer.data_wrapper import Data_Wrapper

class Employee_Logic:
    def __init__(self, data_connection ) -> None:
        self.data_wrapper = data_connection

    def create_employee(self):
        """Takes in Employee object and forwards it to the data layer"""
        self.Employee_Data.create_employee(employee)

    def list_employees(self):
        pass

    def edit_employee(self):
        pass

    def check_working_status(self):
        pass

    def list_voyges_for_an_employee(self):
        pass

    def get_all_employees(self):
        self.Employee_Data.get_all_employees(employee)