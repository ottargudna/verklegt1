import pyfiglet as pfg
from UI_layer.Airplane_menu_UI import Airplane
from UI_layer.Destinations_menu_UI import Desinations
from UI_layer.Employee_menu_UI import Employee
from UI_layer.Voyage_menu_UI import Voyage
from UI_layer.Flights_menu_UI import Flights

BORDER = 109 * "="

class MainMenu_ui:
    def __init__(self) -> None:
        
        self.main_menu = f"""
                                What kind of staff member are you?
                                
                                [1] Manager
                                [2] Shift Supervisor
                                [3] Employee
{BORDER}
        """

        self.options = f"""
                                [B]ack to main menu     [Q]uit
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

        self.manager_and_shift_supervisor_menu = f"""

                                [1] Airplanes
                                [2] Destinations
                                [3] Employees
                                [4] Flights
                                [5] Voyages
{BORDER}
        """

        self.employee_menu = f"""
                                [1] Display Shifts
                                [2] Display Hours
{BORDER}
        """
    
    def employee_name(self):
        return input("Enter your name: ")

    def input_prompt(self):
        return input("Enter your selection: ")
    