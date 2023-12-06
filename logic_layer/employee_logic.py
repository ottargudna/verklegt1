
from Model.employee import Employee
from data_layer.data_wrapper import Data_Wrapper

class Employee_Logic:
    def __init__(self, data_connection ) -> None:
        self.data_wrapper = data_connection

    def create_employee(self, employee):
        """Takes in Employee object and forwards it to the data layer"""
        self.data_wrapper.create_employee(employee)

    def get_all_employees(self):
        """Gets all employees"""
        self.data_wrapper.get_all_employees()

    def list_employees(self):
        pass

    def edit_employee(self):
        pass

    def check_working_status(self):
        pass

    def list_voyges_for_an_employee(self):
        pass