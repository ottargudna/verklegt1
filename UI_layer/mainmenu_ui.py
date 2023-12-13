from UI_layer.Destinations_menu_UI import Destiantions_menu_ui
from UI_layer.Airplane_menu_UI import Airplane_menu_ui
from UI_layer.Employee_menu_UI import Employee_menu_ui
from UI_layer.Voyage_menu_UI import Voyage_menu_ui
import UI_layer.constants

#BORDER = 109 * "="
#QUIT = "q"
#BACK = "b"
#EXIT_TEXT = "Goodbye :)"
#SELECTION_ONE = "1"
#SELECTION_TWO = "2"
#SELECTION_THREE = "3"
#SELECTION_FOUR = "4"
#SELECTION_FIVE = "5"

class MainMenu_ui:
    def __init__(self) -> None:
        self.employee_menu = Employee_menu_ui()
        self.destinations_menu = Destiantions_menu_ui()
        self.airplane_menu = Airplane_menu_ui()
        self.voyage_menu = Voyage_menu_ui()
        self.constants = UI_layer.constants
        
        self.main_menu_man = f"""
                                What kind of staff member are you?
                                
                                [{self.constants.SELECTION_ONE}] Manager
                                [{self.constants.SELECTION_TWO}] Shift Supervisor
                                [{self.constants.SELECTION_THREE}] Employee
{self.constants.BORDER}
        """

#        self.main_menu_options = f"""
#                                [{QUIT}]uit
#        """

#        self.options = f"""
#                                [{BACK}]ack to main menu     [{QUIT}]uit
#{BORDER}
#        """

#        self.ascii_nanair = f"""
#{BORDER}
#                              _    _          _    _       __     _____  _____
#                __|__        |  \ | |   __ _ |  \ | |     /  \   |_   _||  _  \         __|__ 
#            ---o-(_)-o---    |   \| | / __' ||   \| |    / /\ \    | |  | |_|  |    ---o-(_)-o---
#                             | |\   || |__| || |\   |   /  __  \  _| |_ |  _ _/      
#                             |_| \__| \___,_||_| \__|  /__/  \__\|_____||_| \_\ 
#{BORDER}
#        """

        self.manager_menu = f"""

                                [{self.constants.SELECTION_ONE}] Airplanes
                                [{self.constants.SELECTION_TWO}] Destinations
                                [{self.constants.SELECTION_THREE}] Employees
                                [{self.constants.SELECTION_FOUR}] Voyages
{self.constants.BORDER}
        """

        self.shift_supervisor_menu = f"""
                                [{self.constants.SELECTION_ONE}] Destinations
                                [{self.constants.SELECTION_TWO}] Employees
                                [{self.constants.SELECTION_THREE}] Voyages
{self.constants.BORDER}
        """

        self.employee_menu = f"""
                                [{self.constants.SELECTION_ONE}] Display Shifts
                                [{self.constants.SELECTION_TWO}] Display Hours
{self.constants.BORDER}
        """
    
    def employee_name(self):
        return input("Enter your name: ")
    
    def input_prompt(self):
        return input("Enter your selection: ").lower()
    
    def get_shift_superviser(self):
        print(self.constants.ASCII_NANAIR)
        print(self.shift_supervisor_menu)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # List all Destinations
            self.destinations_menu.list_all_destinations()

        elif user_selection == self.constants.SELECTION_TWO: # Employees
            self.employee_menu.get_shift_superviser_employees_menu()

        elif user_selection == self.constants.SELECTION_THREE: # Voyages
            self.voyage_menu.get_shift_superviser_voyage()
        
    
    def get_manager(self):
        print(self.constants.ASCII_NANAIR)
        print(self.manager_menu)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # Airplanes
            self.airplane_menu.get_manager_airplane_menu()

        elif user_selection == self.constants.SELECTION_TWO: # Destinations
            self.destinations_menu.get_manager_destinations()
                
        elif user_selection == self.constants.SELECTION_THREE: # Employees
            self.employee_menu.get_manager_employees_menu()
            #name = input("name")
            #ssn = input("ssn")
            #input("phone")
            #input("enail")
            #logicwrapper.create_empl(Emplpoyee(name, ssn, ...))

        elif user_selection == self.constants.SELECTION_FIVE: # Voyages
            self.voyage_menu.get_manager_voyage()

        elif user_selection == self.constants.QUIT:
            print(self.constants.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    
    def get_employee(self):
        pass
    

    def main(self):

        while True:
            print(self.constants.ASCII_NANAIR)
            print(self.main_menu_man)
            print(self.constants.OPTIONS)
            user_selection = self.input_prompt()
            
            if user_selection == self.constants.QUIT:
                print(self.constants.EXIT_TEXT)
                break
            
            elif user_selection == self.constants.SELECTION_ONE: # Manager
                self.get_manager()
            
            elif user_selection == self.constants.SELECTION_TWO: # Shift superviser
                self.get_shift_superviser()
            
            elif user_selection == self.constants.SELECTION_THREE: # Employee
                self.get_employee()
            

    #elif user_selection == SELECTION_THREE: # Employees
        #name = input("name")
        #ssn = input("ssn")
        #input("phone")
        #input("enail")
        #logicwrapper.create_empl(Emplpoyee(name, ssn, ...))
        #pass

    #if user_selection == SELECTION_ONE: # Display Shifts
        #pass
    #if user_selection == SELECTION_ONE: # Display Shifts
        #pass

    #elif user_selection == SELECTION_TWO: # Display Hours
        #pass
