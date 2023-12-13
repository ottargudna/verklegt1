from Model.employee import Employee
from UI_layer.mainmenu_ui import MainMenu_ui

BORDER = 109 * "*"
QUIT = "q"
BACK = "b"
EXIT_TEXT = "Goodbye :)"
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"


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
                                [{SELECTION_ONE}] Register a new pilot
                                [{SELECTION_TWO}] Edit information of a pilot
                                [{SELECTION_THREE}] Search for a pilot
                                [{SELECTION_FOUR}] List all pilots
{BORDER}
        """
        self.crew_manager = f"""
                                [{SELECTION_ONE}] Register a new crew member
                                [{SELECTION_TWO}] Edit information of a crew member
                                [{SELECTION_THREE}] Search for a crew member
                                [{SELECTION_FOUR}] List all crew members
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
            pass

        elif user_selection == SELECTION_TWO: # List information of an employee
            pass

        elif user_selection == SELECTION_THREE: # List all employees not working on a given day
            pass

        elif user_selection == SELECTION_FOUR: # List all employees working on a given day
            pass

        elif user_selection == SELECTION_FIVE: # Printable work summary for an employee in a giving week
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
            pass

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