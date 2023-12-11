
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

    #def check_working_status(self, date, option):
    """" employees = self.get_all_flights()
        self.data_wrapper = date
        working = []
        not_working = []
        for employee in employees:
            if employee[?] == date:
                    working.append(employee[2])
            else:
                    not_working.append(employee[2])
        if option == "1":
            return working
        else:
             return not_working
"""


    def list_voyges_for_an_employee(self):
        pass

