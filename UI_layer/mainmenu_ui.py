from UI_layer.Employee_menu_UI import Employee_menu_ui
from UI_layer.mainmenu_ui import MainMenu_ui
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
            pass

        elif user_selection == SELECTION_TWO: # Employees
            print(self.ascii_nanair)
            print(self.employee_menu.main_menu)
            print(self.options)
            user_selection = self.input_prompt()

            if user_selection == SELECTION_ONE:
                pass

            elif user_selection == SELECTION_TWO:
                pass

        elif user_selection == SELECTION_THREE: # Voyages
            pass
        
    
    def get_manager(self):
        print(self.ascii_nanair)
        print(self.manager_menu)
        print(self.options)
        user_selection = self.input_prompt()

        if user_selection == SELECTION_ONE: # Airplanes
            print(self.ascii_nanair)
            print(self.airplane_menu.manager_menu)
            print(self.options)
            user_selection = self.input_prompt()

            if user_selection == SELECTION_ONE: # Register airplane
                pass

            elif user_selection == SELECTION_TWO: # Edit airplane
                pass

            elif user_selection == QUIT:
                print(EXIT_TEXT)
                quit()
            
            else: # Go back
                pass

        elif user_selection == SELECTION_TWO: # Destinations
                print(self.ascii_nanair)
                print(self.destinations_menu.manager_menu)
                print(self.options)
                user_selection = self.input_prompt()

                if user_selection == SELECTION_ONE: # Register a new destination
                    pass
                
                elif user_selection == SELECTION_TWO: # Edit destinations
                    pass

                elif user_selection == SELECTION_THREE: # List all destinations
                    pass

                elif user_selection == QUIT:
                    print(EXIT_TEXT)
                    quit()
            
                else: # Go back
                    pass
                
        elif user_selection == SELECTION_THREE: # Employees
            print(self.ascii_nanair)
            print(self.employee_menu.main_menu)
            print(self.options)
            user_selection = self.input_prompt()

            if user_selection == SELECTION_ONE: # List all employees
                pass
            
            elif user_selection == SELECTION_TWO: # Pilot
                print(self.ascii_nanair)
                print(self.employee_menu.pilot_menu)
                print(self.options)
                user_selection = self.input_prompt()

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

            elif user_selection == SELECTION_THREE: # Crew
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

        elif user_selection == SELECTION_FIVE: # Voyages
            print(self.ascii_nanair)
            print(self.voyage_menu.voyage_menu_manager)
            print(self.options)
            user_selection = self.input_prompt()

            if user_selection == SELECTION_ONE: # Register a new voyage
                pass

            elif user_selection == SELECTION_TWO: # List all voyages
                pass

            elif user_selection == SELECTION_THREE: # List all voyages for a given day
                pass

            elif user_selection == SELECTION_FOUR: # List all voyages for a given week
                pass

            elif user_selection == SELECTION_FIVE: # List all voyages of a staff member for a given week
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
