
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

    def edit_employee(self, employee):
        '''Takes in name of an employee and forwards it to data layer'''
        self.data_wrapper.edit_employee(employee)
        
        
    def list_voyges_for_an_employee(self):
        pass

