
from Model.employee import Employee
from data_layer.data_wrapper import Data_Wrapper
from datetime import datetime, timedelta


class Employee_Logic:
    def __init__(self, data_connection ) -> None:
        self.data_wrapper = data_connection

    def create_employee(self, employee):
        """Takes in Employee object and forwards it to the data layer"""
        every_employee = self.data_wrapper.get_all_employees()
        for e in every_employee:
            if employee.nid == e.nid:
                return False #already exists
        self.data_wrapper.create_employee(employee)

    def get_all_employees(self):
        """Gets all employees"""
        self.data_wrapper.get_all_employees()

    def edit_employee(self, employee):
        '''Takes in name of an employee and forwards it to data layer'''
        self.data_wrapper.edit_employee(employee)
        
        
    def list_voyges_for_an_employee(self):
        pass

    def get_one_employee(self, nid):
        '''searches for one employee'''
        every_employee = self.data_wrapper.get_all_employees()
        for employee in every_employee:
            if employee.nid == nid:
                return employee
            
    def date_time(self, date):
        '''gets date and time, splits it and makes so you can calculate'''
            #date is an str yyyy.mm.dd
            #we need to split it
        try:
            year, month, day = map(int, date.split("."))
            result_date = datetime(year, month, day)
            return result_date
        except ValueError:
            return False

    def date_time_plus_week(self, date):
        '''adds 7 days to a date thefore a week'''
        int_date = self.date_time(date)

        week_from_date = int_date + timedelta(days=6)

        return week_from_date


    def get_week_work(self, nid, date):
        '''Gets a list of voyages that the nid is working on'''

        #get every employee and voyage
        voyages = self.data_wrapper.get_all_voyages()
        every_employee = self.data_wrapper.get_all_employees()

        date = self.date_time(date)
        week_from_date = self.date_time_plus_week(date)

        voyages_in_date = []

        for voyage in voyages:
            date_out = self.date_time(voyage.date_out)
            date_home = self.date_time(voyage.date_home)
            if  date <= date_out <= week_from_date or date <= date_home <= week_from_date :
                voyages_in_date.append(voyage)

        workin_in_voyage = []

        for voyage in voyages_in_date:
            if nid == voyage.captain or nid == voyage.copilot or nid == voyage.flight_service_manager or nid == voyage.flight_attendant1 or nid == voyage.flight_attendant2:
                workin_in_voyage.append(voyage)

        return workin_in_voyage




        
