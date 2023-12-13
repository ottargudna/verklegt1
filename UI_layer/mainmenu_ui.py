from UI_layer.Employee_menu_UI import Employee_menu_ui
from UI_layer.Destinations_menu_UI import Destiantions_menu_ui
from UI_layer.Airplane_menu_UI import Airplane_menu_ui
from UI_layer.Voyage_menu_UI import Voyage_menu_ui

BORDER = 109 * "="
QUIT = "q"
BACK = "b"
EXIT_TEXT = "Goodbye :)"
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"


class MainMenu_ui:
    def __init__(self) -> None:
        self.employee_menu = Employee_menu_ui()
        self.destinations_menu = Destiantions_menu_ui()
        self.airplane_menu = Airplane_menu_ui()
        self.voyage_menu = Voyage_menu_ui()
        
        self.main_menu = f"""
                                What kind of staff member are you?
                                
                                [{SELECTION_ONE}] Manager
                                [{SELECTION_TWO}] Shift Supervisor
                                [{SELECTION_THREE}] Employee
{BORDER}
        """

        self.main_menu_options = f"""
                                [{QUIT}]uit
        """

        self.options = f"""
                                [{BACK}]ack to main menu     [{QUIT}]uit
{BORDER}
        """

        self.ascii_nanair = f"""
{BORDER}
                              _    _          _    _       __     _____  _____
                __|__        |  \ | |   __ _ |  \ | |     /  \   |_   _||  _  \         __|__ 
            ---o-(_)-o---    |   \| | / __' ||   \| |    / /\ \    | |  | |_|  |    ---o-(_)-o---
                             | |\   || |__| || |\   |   /  __  \  _| |_ |  _ _/      
                             |_| \__| \___,_||_| \__|  /__/  \__\|_____||_| \_\ 
{BORDER}
        """

        self.manager_menu = f"""

                                [{SELECTION_ONE}] Airplanes
                                [{SELECTION_TWO}] Destinations
                                [{SELECTION_THREE}] Employees
                                [{SELECTION_FOUR}] Voyages
{BORDER}
        """

        self.shift_supervisor_menu = f"""
                                [{SELECTION_ONE}] Destinations
                                [{SELECTION_TWO}] Employees
                                [{SELECTION_THREE}] Voyages
{BORDER}
        """

        self.employee_menu = f"""
                                [{SELECTION_ONE}] Display Shifts
                                [{SELECTION_TWO}] Display Hours
{BORDER}
        """
    
    def employee_name(self):
        return input("Enter your name: ")
    
    def input_prompt(self):
        return input("Enter your selection: ").lower()
    
    def get_shift_superviser(self):
        print(self.ascii_nanair)
        print(self.shift_supervisor_menu)
        print(self.options)
        user_selection = self.input_prompt()

        if user_selection == SELECTION_ONE: # List all Destinations
            self.destinations_menu.list_all_destinations()

        elif user_selection == SELECTION_TWO: # Employees
            self.employee_menu.get_shift_superviser_employees_menu()

        elif user_selection == SELECTION_THREE: # Voyages
            pass
        
    
    def get_manager(self):
        print(self.ascii_nanair)
        print(self.manager_menu)
        print(self.options)
        user_selection = self.input_prompt()

        if user_selection == SELECTION_ONE: # Airplanes
            self.airplane_menu.get_manager_airplane_menu()

        elif user_selection == SELECTION_TWO: # Destinations
            self.destinations_menu.get_manager_destinations()
                
        elif user_selection == SELECTION_THREE: # Employees
            self.employee_menu.get_manager_employees_menu()

        elif user_selection == SELECTION_FIVE: # Voyages
            pass

        elif user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    
    def get_employee(self):
        pass
    
def main(self): # I will change the name 
    while True:
        print(self.ascii_nanair)
        print(self.main_menu)
        print(self.main_menu_options)
        user_selection = self.input_prompt()

        if user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
        
        elif user_selection == SELECTION_TWO: # Shift supervisor
            print(self.ascii_nanair)
            print(self.manager_and_shift_supervisor_menu)
            print(self.options)
            user_selection = self.input_prompt()

            if user_selection == SELECTION_ONE: # Airplanes
                print(self.airplane_menu.ascii_nanair)
                print(self.airplane_menu.list_menu)
                print(self.main_menu.options)
                user_selection = self.input_prompt()
                
            elif user_selection == SELECTION_TWO: # Destinations
                pass

            elif user_selection == SELECTION_THREE: # Employees
                #name = input("name")
                #ssn = input("ssn")
                #input("phone")
                #input("enail")
                #logicwrapper.create_empl(Emplpoyee(name, ssn, ...))
                pass    

            elif user_selection == SELECTION_FOUR: # Flights
                pass

            elif user_selection == SELECTION_FIVE: # Voyages
                pass

            elif user_selection == QUIT:
                quit()
            
            else: # Go back
                break

        elif user_selection == SELECTION_THREE: # Employee
            print(self.main_menu.ascii_nanair)
            print(self.main_menu.employee_name())
            print(self.main_menu.employee_menu)
            print(self.main_menu.options)
            user_selection = self.input_prompt()

            if user_selection == SELECTION_ONE: # Display Shifts
                pass
            if user_selection == SELECTION_ONE: # Display Shifts
                pass

            elif user_selection == SELECTION_TWO: # Display Hours
                pass

            elif user_selection == QUIT:
                quit()
            
            else: # Go back
                pass
        
        elif user_selection == QUIT:
            quit()
            
        else: # Go back
            pass
