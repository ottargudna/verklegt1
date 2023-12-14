from Model.employee import Employee
from UI_layer.input_validate import Validate
import UI_layer.constants

class Employee_menu_ui:

    def __init__(self) -> None:
        self.const = UI_layer.constants

    def get_manager_employees_menu(self):
        print(self.main_menu.ascii_nanair)
        print(self.main_menu)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()
        
        if user_selection == self.const.ONE: # Employees
            self.get_employees()
            
        elif user_selection == self.const.TWO: # Pilot
            self.get_manager_pilots()
            
        elif user_selection == self.const.THREE: # Crew
            self.get_manager_crew()
        
        elif user_selection == self.constQUIT:
            print(self.const.self.const.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    

    def get_employees(self):
        print(self.main_menu.ascii_nanair)
        print(self.employees_menu)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == self.const.ONE: # List all employees
            self.get_list_employees()
            

        elif user_selection == self.const.TWO: # List information of an employee
            self.search_employee()

        elif user_selection == self.const.THREE: # List all employees not working on a given day
            self.working_given_day()

        elif user_selection == self.const.FOUR: # List all employees working on a given day
            
            date = input("Enter date: YYYY-MM-DD")

#            check_day = self.logic_wrapper.check_day(date)
#            while check_day == False:
#                print("Enter a valid date:")
#                date = input("Enter date: YYYY-MM-DD")
#            print("List of employees working on a given day:")
#            date_employee = PrettyTable('Date', 'Name', 'NID')
#            for i in check_day:
#                date_employee.add_row([date, i.name, i.nid])

        elif user_selection == self.const.FIVE: # Printable work summary for an employee in a giving week
            
            week = input("Enter NID:")

        elif user_selection == self.const.SIX: #update employee
            pass

        elif user_selection == self.const.QUIT:
            print(self.const.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    

    def get_manager_pilots(self):
        print(self.main_menu.ascii_nanair)
        print(self.pilot_manager)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == self.const.ONE: # Register a new pilot
            pass

        elif user_selection == self.const.TWO: # Edit information of a pilot
            pass

        elif user_selection == self.const.THREE: # Search for a pilot
            
            NID = input("Enter NID to get Pilot: ")
#            while self.input_validate.validate_nid(NID) == False:
#                print('Invalid NID, please try again.')
#                NID = input('Enter NID to get Employee: ')

#            get_one_employee = self.logic_wrapper.get_one_employee(NID)
#            print("List of information of an Employee")
#            info_employee = PrettyTable(['NID','Name','Role','Rank', 'Licence', 'Address', 'Phone_nr', 'Email', 'Homephone_nr'])
#            for i in get_one_employee:
#                info_employee.add_row([i.nid, i.name, i.role, i.rank, i.licence, i.address, i.phone_nr, i.email, i.homephone_nr])
#            print(info_employee)
#            input("Press any key to go back to Employees Menu.")

        elif user_selection == self.const.FOUR: # List pilots
            pass

        elif user_selection == self.const.QUIT:
            print(self.const.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass


    def get_manager_crew(self):
        print(self.main_menu.ascii_nanair)
        print(self.crew_manager)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == self.const.ONE: # Register a new crew member
            pass

        elif user_selection == self.const.TWO: # Edit information of a crew member
            pass

        elif user_selection == self.const.THREE: # Search for a crew member
            pass

        elif user_selection == self.const.FOUR: # List crew members
            pass

        elif user_selection == self.const.QUIT:
            print(self.const.EXIT_TEXT)
            quit()
    
        else: # Go back
            pass
        
    
    def get_shift_superviser_employees_menu(self):
        print(self.main_menu.ascii_nanair)
        print(self.main_menu)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == self.const.ONE: # Employees
            self.get_employees()

        elif user_selection == self.const.TWO: # Pilot
            self.get_shift_superviser_pilots()

        elif user_selection == self.const.THREE: # Crew
            self.get_shift_superviser_crew()
        
        elif user_selection == self.const.QUIT:
            print(self.const.EXIT_TEXT)
            quit()
    
        else: # Go back
            pass


    def get_shift_superviser_pilots(self):
        print(self.main_menu.ascii_nanair)
        print(self.pilot_shift_supervisor)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == self.const.ONE: # Search for a pilot
            pass

        elif user_selection == self.const.TWO: # List all pilots
            pass

        elif user_selection == self.const.QUIT:
            print(self.const.EXIT_TEXT)
            quit()
    
        else: # Go back
            pass


    def get_shift_superviser_crew(self):
        print(self.main_menu.ascii_nanair)
        print(self.crew_shift_supervisor)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == self.const.ONE: # Search for a crew member
            pass

        elif user_selection == self.const.TWO: # List all crew members
            pass

        elif user_selection == self.const.QUIT:
            print(self.const.EXIT_TEXT)
            quit()
    
        else: # Go back
            pass


    def get_list_employees(self):
        result = self.logic_wrapper.get_all_employees()
        print("List of all Employees:")
        All_employees = PrettyTable(['Name', 'Social Id', 'Job Title', 'Rank'])
        for i in result:
            All_employees.add_row([i.name, i.nid, i.role, i.rank])
        print(All_employees)
        input("Press any key to go back to Employees Menu.")
    

    def register_new_employee(self):
        pass

    def edit_employee(self):
        pass

    def list_voyges_for_an_employee(self):
        pass

    def list_voyges_for_employee(self):
        pass

    def search_employee(self):
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


    def working_given_day(self): # We need to change this
        date = input("Enter date: YYYY-MM-DD")
        check_day = self.logic_wrapper.check_day(date)
        while check_day == False:
            print("Enter a valid date:")
            date = input("Enter date: YYYY-MM-DD")
        print("List of all employees not working on a given day:")
        not_working = PrettyTable(check_day[1])
        print(not_working)

    def employee_voyage_week(self):
        pass