from prettytable import PrettyTable
from Model.employee import Employee
from UI_layer.mainmenu_ui import MainMenu_ui
from UI_layer.input_validate import Validate

BORDER = 109 * "*"
QUIT = "q"
BACK = "b"
EXIT_TEXT = "Goodbye :)"
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"
SELECTION_SIX = "6"


class Employee_menu_ui:

    def __init__(self) -> None:
        self.main_menu = MainMenu_ui()
        
        self.main_menu = f"""
                                [1] Employees
                                [2] Pilot
                                [3] Crew
        {BORDER}
        """

        self.pilot_manager = f"""
                                [{SELECTION_ONE}] Edit information of a pilot
                                [{SELECTION_TWO}] Search for a pilot
                                [{SELECTION_THREE}] List all pilots
{BORDER}
        """
        self.crew_manager = f"""
                                [{SELECTION_ONE}] Edit information of a crew member
                                [{SELECTION_TWO}] Search for a crew member
                                [{SELECTION_THREE}] List all crew members
{BORDER}
        """

        self.pilot_shift_supervisor = f"""
                                [{SELECTION_ONE}] Search for a pilot
                                [{SELECTION_TWO}] List all pilots
{BORDER}
        """

        self.crew_shift_supervisor = f"""
                                [{SELECTION_ONE}] Search for a crew member
                                [{SELECTION_TWO}] List all crew members
{BORDER}
        """

        self.employees_menu = f"""
                                [{SELECTION_ONE}] List all employees
                                [{SELECTION_TWO}] List information of an employee
                                [{SELECTION_THREE}] List all employees not working on a given day
                                [{SELECTION_FOUR}] List all employees working on a given day
                                [{SELECTION_FIVE}] Printable work summary for an employee in a giving week
                                [{SELECTION_SIX}] Register new employee
{BORDER}
        """
    

    def get_manager_employees_menu(self):
        print(self.main_menu.ascii_nanair)
        print(self.main_menu)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()
        
        if user_selection == SELECTION_ONE: # Employees
            self.get_employees()
            
        elif user_selection == SELECTION_TWO: # Pilot
            self.get_manager_pilots()
            
        elif user_selection == SELECTION_THREE: # Crew
            self.get_manager_crew()
        
        elif user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    

    def get_employees(self):
        print(self.main_menu.ascii_nanair)
        print(self.employees_menu)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == SELECTION_ONE: # List all employees

            result = self.logic_wrapper.get_all_employees()
            print("List of all Employees:")
            All_employees = PrettyTable(['Name', 'Social Id', 'Job Title', 'Rank'])
            for i in result:
                All_employees.add_row([i.name, i.nid, i.role, i.rank])
            print(All_employees)
            input("Press any key to go back to Employees Menu.")

        elif user_selection == SELECTION_TWO: # List information of an employee
            
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

        elif user_selection == SELECTION_THREE: # List all employees not working on a given day
            
            date = input("Enter date: YYYY-MM-DD")
            check_day = self.logic_wrapper.check_day(date)
            while check_day == False:
                print("Enter a valid date:")
                date = input("Enter date: YYYY-MM-DD")
            print("List of all employees not working on a given day:")
            not_working = PrettyTable(check_day[1])
            print(not_working)

        elif user_selection == SELECTION_FOUR: # List all employees working on a given day
            
            date = input("Enter date: YYYY-MM-DD")

            check_day = self.logic_wrapper.check_day(date)
            while check_day == False:
                print("Enter a valid date:")
                date = input("Enter date: YYYY-MM-DD")
            print("List of employees working on a given day:")
            date_employee = PrettyTable('Date', 'Name', 'NID')
            for i in check_day:
                date_employee.add_row([date, i.name, i.nid])

        elif user_selection == SELECTION_FIVE: # Printable work summary for an employee in a giving week
            
            week = input("Enter NID:")

        elif user_selection == SELECTION_SIX: #update employee
            pass

        elif user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    

    def get_manager_pilots(self):
        print(self.main_menu.ascii_nanair)
        print(self.pilot_manager)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == SELECTION_ONE: # Register a new pilot
            pass

        elif user_selection == SELECTION_TWO: # Edit information of a pilot
            pass

        elif user_selection == SELECTION_THREE: # Search for a pilot
            
            NID = input("Enter NID to get Pilot: ")
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

        elif user_selection == SELECTION_FOUR: # List pilots
            pass

        elif user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
        
        else: # Go back
            pass


    def get_manager_crew(self):
        print(self.main_menu.ascii_nanair)
        print(self.crew_manager)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == SELECTION_ONE: # Register a new crew member
            pass

        elif user_selection == SELECTION_TWO: # Edit information of a crew member
            pass

        elif user_selection == SELECTION_THREE: # Search for a crew member
            pass

        elif user_selection == SELECTION_FOUR: # List crew members
            pass

        elif user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
    
        else: # Go back
            pass
        
    
    def get_shift_superviser_employees_menu(self):
        print(self.main_menu.ascii_nanair)
        print(self.main_menu)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == SELECTION_ONE: # Employees
            self.get_employees()

        elif user_selection == SELECTION_TWO: # Pilot
            self.get_shift_superviser_pilots()

        elif user_selection == SELECTION_THREE: # Crew
            self.get_shift_superviser_crew()
        
        elif user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
    
        else: # Go back
            pass


    def get_shift_superviser_pilots(self):
        print(self.main_menu.ascii_nanair)
        print(self.pilot_shift_supervisor)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == SELECTION_ONE: # Search for a pilot
            pass

        elif user_selection == SELECTION_TWO: # List all pilots
            pass

        elif user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
    
        else: # Go back
            pass


    def get_shift_superviser_crew(self):
        print(self.main_menu.ascii_nanair)
        print(self.crew_shift_supervisor)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == SELECTION_ONE: # Search for a crew member
            pass

        elif user_selection == SELECTION_TWO: # List all crew members
            pass

        elif user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
    
        else: # Go back
            pass

    # List all employees
    def get_list_employees(self):
        pass

    # List information of an employee
    # List all employees not working on a given day
    # List all employees working on a given day
    # Printable work summary for an employee in a giving week
    # Register a new crew member
    # Edit information of a crew member
    # Search for a crew member
    # List crew members
    # Register a new pilot
    # Edit information of a pilot
    # Search for a pilot
    # List pilots