import pyfiglet as pfg
from UI_layer.Airplane_menu_UI import Airplane
from UI_layer.Destinations_menu_UI import Desinations
from UI_layer.Employee_menu_UI import Employee
from UI_layer.Voyage_menu_UI import Voyage
from UI_layer.Flights_menu_UI import Flights

BORDER = 50 * "=" # I´m not sure if this is a long enough border
ASCII_ART = """ 
                __|__
            ---o-(_)-o--- 
        """
ASCII_NANAIR = pfg.figlet_format("NaN AIR", font="slant")

class MainMenu_ui:
    def __init__(self) -> None:
        pass

    def staff_member_menu(self) -> None:
        print(BORDER)
        print(ASCII_ART)
        print(ASCII_NANAIR)
        print("What kind of staff member are you?")
        print("[1] Manager")
        print("[2] Shift Supervisor")
        print("[3] Employee")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(BORDER)

        self.input_prompt(self)

    def manager_and_shift_supervisor_menu(self):
        print(BORDER)
        print("[1] Airplanes")
        print("[2] Destinations")
        print("[3] Employees")
        print("[4] Flights")
        print("[5] Voyages")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(BORDER)
    
    def employee_name(self): # We might have to move this function to another class
        return input("Enter your name: ")
    
    def employee_menu(self):
        print(BORDER)
        print("[1] Display Shifts")
        print("[2] Display Hours")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(BORDER)

        self.input_prompt(self)

    def input_prompt(self):
        return input("Enter your selection: ")