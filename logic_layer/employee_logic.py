
from Model.employee import Employee
from data_layer.data_wrapper import Data_Wrapper
from datetime import datetime, timedelta


class Employee_Logic:
    def __init__(self, data_connection ) -> None:
        self.datawrapper = Data_Wrapper()
        self.data_wrapper = data_connection

    def create_employee(self, employee):
        """Takes in Employee object and forwards it to the data layer"""
        every_employee = self.data_wrapper.datawrapper.get_all_employees()
        for e in every_employee:
            if employee.nid == e.nid:
                return False #already exists
        self.datawrapper.create_employee(employee)

    def get_all_employees(self):
        """Gets all employees"""
        employees_list = []
        employees = self.datawrapper.get_all_employees()
        for employee in employees:
            employees_list.append([employee.role, employee.nid, employee.name])
        return employees_list

    def edit_employee(self, employee):
        '''Takes in name of an employee and forwards it to data layer'''
        self.datawrapper.update_employee(employee)
        
        
    def list_voyges_for_an_employee(self):
        pass
    
    def get_one_employee(self, nid):
        '''searches for one employee'''
        employee_list = []
        every_employee = self.datawrapper.get_all_employees()
        for employee in every_employee:
            if employee.nid == nid:
                employee_list.append(employee)
        return employee_list
            
    def date_time(self, date):
        '''gets date and time, splits it and makes so you can calculate'''
            #date is an str yyyy.mm.dd
            #we need to split it
        try:
            year, month, day = map(int, date.split("."))
            result_date = datetime(year, month, day)
            return result_date
        except ValueError:
            return None

    def date_time_plus_week(self, date):
        '''adds 7 days to a date thefore a week'''
        try:
            if date == None:
                return None
            else:
                week_from_date = date + timedelta(days=7)
            return week_from_date
        except ValueError or TypeError:
            return None


    def get_week_work(self, nid, date):
        '''Gets a list of voyages that the nid is working on'''

        #get every employee and voyage
        voyages = self.datawrapper.get_all_voyages()
        
        date = self.date_time(date)
        week_from_date = self.date_time_plus_week(date)

        if date == None or week_from_date == None:
            return False
        
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
    

    def check_if_voyages_are_fully_shiped(self):
        '''Cheks if user has a voyage where there is not an a employee in it'''
        voyages = self.datawrapper.get_all_voyages()

        not_fully_shiped = []


        for voyage in voyages:
            if voyage.captain == "N/A":
                if voyage not in not_fully_shiped:
                    not_fully_shiped.append(voyage)
            elif voyage.copilot == "N/A":
                if voyage not in not_fully_shiped:
                    not_fully_shiped.append(voyage)
            elif voyage.flight_service_manager == "N/A":
                if voyage not in not_fully_shiped:
                    not_fully_shiped.append(voyage)
            elif voyage.flight_attendant1 == "N/A":
                if voyage not in not_fully_shiped:
                    not_fully_shiped.append(voyage)
            elif voyage.flight_attendant2 == "N/A":
                if voyage not in not_fully_shiped:
                    not_fully_shiped.append(voyage)
        
        if not_fully_shiped == None:
            return False
        
        return not_fully_shiped



