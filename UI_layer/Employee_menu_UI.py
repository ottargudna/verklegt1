from Model.employee import Employee
from UI_layer.input_validate import Validate
import UI_layer.constants
from logic_layer.logic_wrapper import Logic_Wrapper
from prettytable import PrettyTable

class Employee_menu_ui:

    def __init__(self) -> None:
        self.const = UI_layer.constants
        self.logic_wrapper = Logic_Wrapper()
        self.input_validate = Validate()
    

    def get_employees(self):
        print(self.const.employees_menu())
        user_selection = self.const.input_selection()

        if user_selection == self.const.ONE: # List all employees
            self.get_list_employees()
            
        elif user_selection == self.const.TWO: # List information of an employee
            self.search_employee()

        elif user_selection == self.const.THREE: # List all employees not working on a given day
            self.not_working_given_day()

        elif user_selection == self.const.FOUR: # List all employees working on a given day
            self.get_working_given_day()

        elif user_selection == self.const.FIVE: # Printable work summary for an employee in a giving week
            self.employees_working_week()

        elif user_selection == self.const.SIX: #update employee
            self.edit_employee()

        elif user_selection == self.const.QUIT:
            print(self.const.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass


    def get_list_employees(self): # We need to change this
        result = self.logic_wrapper.get_all_employees()
        print("List of all Employees:")
        all_employees = PrettyTable(['Name', 'Social Id', 'Job Title', 'Rank'])
        for i in result:
            all_employees.add_row([i.name, i.nid, i.role, i.rank])
        print(all_employees)
        input("Press any key to go back to Employees Menu.")
    

    def register_new_employee(self):
        pass

    def edit_employee(self):
        pass

    def list_voyges_for_employee(self):
        pass

    def search_employee(self): # We need to change this
        NID = input("Enter NID to get Employee: ")
        while self.input_validate.validate_nid(NID) == False:
            print('Invalid NID, please try again.')
            NID = input('Enter NID to get Employee: ')

        get_one_employee = self.logic_wrapper.get_one_employee(NID)
        print("List of information of an Employee")
        info_employee = PrettyTable(['NID','Name','Role','Rank', 'Licence', 'Address', 'Phone_nr', 'Email', 'Homephone_nr'])
        for i in get_one_employee:
            info_employee.add_row([i.nid, i.name, i.role, i.rank, i.licence, i.address, i.phone_nr, i.email, i.homephone_nr])
        print(info_employee)
        input("Press any key to go back to Employees Menu.")


    def not_working_given_day(self): # We need to change this
        date = input("Enter date: YYYY-MM-DD")
        check_day = self.logic_wrapper.check_day(date)
        while check_day == False:
            print("Enter a valid date:")
            date = input("Enter date: YYYY-MM-DD")
        print("List of all employees not working on a given day:")
        not_working = PrettyTable(check_day[1])
        print(not_working)
    

    def get_working_given_day(self): # We need to change this
        date = input("Enter date: YYYY-MM-DD")

        check_day = self.logic_wrapper.check_day(date)
        while check_day == False:
            print("Enter a valid date:")
            date = input("Enter date: YYYY-MM-DD")
        print("List of employees working on a given day:")
        date_employee = PrettyTable('Date', 'Name', 'NID')
        for i in check_day:
            date_employee.add_row([date, i.name, i.nid])


    def employees_working_week(self):
        week = input("Enter NID:")

    
#    def get_search_pilot(self): # We need to change this
#        NID = input("Enter NID to get Pilot: ")
#        while self.input_validate.validate_nid(NID) == False:
#            print('Invalid NID, please try again.')
#            NID = input('Enter NID to get Employee: ')
#
#        get_one_employee = self.logic_wrapper.get_one_employee(NID)
#        print("List of information of an Employee")
#        info_employee = PrettyTable(['NID','Name','Role','Rank', 'Licence', 'Address', 'Phone_nr', 'Email', 'Homephone_nr'])
#        for i in get_one_employee:
#            info_employee.add_row([i.nid, i.name, i.role, i.rank, i.licence, i.address, i.phone_nr, i.email, i.homephone_nr])
#        print(info_employee)
#        input("Press any key to go back to Employees Menu.")