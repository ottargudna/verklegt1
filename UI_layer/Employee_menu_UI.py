#from Model.employee import Employee
import UI_layer.constants

#BORDER = 109 * "*"
#QUIT = "q"
#BACK = "b"
#EXIT_TEXT = "Goodbye :)"
#SELECTION_ONE = "1"
#SELECTION_TWO = "2"
#SELECTION_THREE = "3"
#SELECTION_FOUR = "4"
#SELECTION_FIVE = "5"


class Employee_menu_ui:

    def __init__(self) -> None:
        #self.main_menu = MainMenu_ui()
        self.constants = UI_layer.constants
        
        self.main_menu = f"""
                                [1] Employees
                                [2] Pilot
                                [3] Crew
        {self.constants.BORDER}
        """

        self.pilot_manager = f"""
                                [{self.constants.SELECTION_ONE}] Register a new pilot
                                [{self.constants.SELECTION_TWO}] Edit information of a pilot
                                [{self.constants.SELECTION_THREE}] Search for a pilot
                                [{self.constants.SELECTION_FOUR}] List all pilots
{self.constants.BORDER}
        """
        self.crew_manager = f"""
                                [{self.constants.SELECTION_ONE}] Register a new crew member
                                [{self.constants.SELECTION_TWO}] Edit information of a crew member
                                [{self.constants.SELECTION_THREE}] Search for a crew member
                                [{self.constants.SELECTION_FOUR}] List all crew members
{self.constants.BORDER}
        """

        self.pilot_shift_supervisor = f"""
                                [{self.constants.SELECTION_ONE}] Search for a pilot
                                [{self.constants.SELECTION_TWO}] List all pilots
{self.constants.BORDER}
        """

        self.crew_shift_supervisor = f"""
                                [{self.constants.SELECTION_ONE}] Search for a crew member
                                [{self.constants.SELECTION_TWO}] List all crew members
{self.constants.BORDER}
        """

        self.employees_menu = f"""
                                [{self.constants.SELECTION_ONE}] List all employees
                                [{self.constants.SELECTION_TWO}] List information of an employee
                                [{self.constants.SELECTION_THREE}] List all employees not working on a given day
                                [{self.constants.SELECTION_FOUR}] List all employees working on a given day
                                [{self.constants.SELECTION_FIVE}] Printable work summary for an employee in a giving week
{self.constants.BORDER}
        """
    

    def get_manager_employees_menu(self):
        print(self.constants.ASCII_NANAIR)
        print(self.main_menu)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT
        
        if user_selection == self.constants.SELECTION_ONE: # Employees
            self.get_employees()
            
        elif user_selection == self.constants.SELECTION_TWO: # Pilot
            self.get_manager_pilots()
            
        elif user_selection == self.constants.SELECTION_THREE: # Crew
            self.get_manager_crew()
        
        elif user_selection == self.constants.QUIT:
            print(self.constants.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    

    def get_employees(self):
        print(self.constants.ASCII_NANAIR)
        print(self.employees_menu)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # List all employees
            pass

        elif user_selection == self.constants.SELECTION_TWO: # List information of an employee
            pass

        elif user_selection == self.constants.SELECTION_THREE: # List all employees not working on a given day
            pass

        elif user_selection == self.constants.SELECTION_FOUR: # List all employees working on a given day
            pass

        elif user_selection == self.constants.SELECTION_FIVE: # Printable work summary for an employee in a giving week
            pass

        elif user_selection == self.constants.QUIT:
            print(self.constants.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    

    def get_manager_pilots(self):
        print(self.constants.ASCII_NANAIR)
        print(self.pilot_manager)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # Register a new pilot
            pass

        elif user_selection == self.constants.SELECTION_TWO: # Edit information of a pilot
            pass

        elif user_selection == self.constants.SELECTION_THREE: # Search for a pilot
            pass

        elif user_selection == self.constants.SELECTION_FOUR: # List pilots
            pass

        elif user_selection == self.constants.QUIT:
            print(self.constants.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass


    def get_manager_crew(self):
        print(self.constants.ASCII_NANAIR)
        print(self.crew_manager)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # Register a new crew member
            pass

        elif user_selection == self.constants.SELECTION_TWO: # Edit information of a crew member
            pass

        elif user_selection == self.constants.SELECTION_THREE: # Search for a crew member
            pass

        elif user_selection == self.constants.SELECTION_FOUR: # List crew members
            pass

        elif user_selection == self.constants.QUIT:
            print(self.constants.EXIT_TEXT)
            quit()
    
        else: # Go back
            pass
        
    
    def get_shift_superviser_employees_menu(self):
        print(self.constants.ASCII_NANAIR)
        print(self.main_menu)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # Employees
            self.get_employees()

        elif user_selection == self.constants.SELECTION_TWO: # Pilot
            self.get_shift_superviser_pilots()

        elif user_selection == self.constants.SELECTION_THREE: # Crew
            self.get_shift_superviser_crew()
        
        elif user_selection == self.constants.QUIT:
            print(self.constants.EXIT_TEXT)
            quit()
    
        else: # Go back
            pass


    def get_shift_superviser_pilots(self):
        print(self.constants.ASCII_NANAIR)
        print(self.pilot_shift_supervisor)
        print(self.constants.ASCII_NANAIR)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # Search for a pilot
            pass

        elif user_selection == self.constants.SELECTION_TWO: # List all pilots
            pass

        elif user_selection == self.constants.QUIT:
            print(self.constants.EXIT_TEXT)
            quit()
    
        else: # Go back
            pass


    def get_shift_superviser_crew(self):
        print(self.constants.ASCII_NANAIR)
        print(self.crew_shift_supervisor)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # Search for a crew member
            pass

        elif user_selection == self.constants.SELECTION_TWO: # List all crew members
            pass

        elif user_selection == self.constants.QUIT:
            print(self.constants.EXIT_TEXT)
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