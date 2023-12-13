from UI_layer.Employee_menu_UI import Employee_menu_ui
from UI_layer.Destinations_menu_UI import Destiantions_menu_ui
from UI_layer.Airplane_menu_UI import Airplane_menu_ui
from UI_layer.Voyage_menu_UI import Voyage_menu_ui
import UI_layer.constants

class MainMenu_ui:
    def __init__(self) -> None:
        self.employee_menu = Employee_menu_ui()
        self.destinations_menu = Destiantions_menu_ui()
        self.airplane_menu = Airplane_menu_ui()
        self.voyage_menu = Voyage_menu_ui()
        self.const = UI_layer.constants
    
    def employee_name(self):
        return input("Enter your name: ")
    
    def input_prompt(self):
        return input("Enter your selection: ").lower()
    
    def get_shift_superviser(self):
        print(self.ascii_nanair)
        print(self.shift_supervisor_menu)
        print(self.options)
        user_selection = self.input_prompt()

        if user_selection == self.const.ONE: # List all Destinations
            self.destinations_menu.list_all_destinations()

        elif user_selection == self.const.TWO: # Employees
            self.employee_menu.get_shift_superviser_employees_menu()

        elif user_selection == self.const.THREE: # Voyages
            self.voyage_menu.get_shift_superviser_voyage()
        
    
    def get_manager(self):
        print(self.ascii_nanair)
        print(self.manager_menu)
        print(self.options)
        user_selection = self.input_prompt()

        if user_selection == self.const.ONE: # Airplanes
            self.airplane_menu.get_manager_airplane_menu()

        elif user_selection == self.const.TWO: # Destinations
            self.destinations_menu.get_manager_destinations()
                
        elif user_selection == self.const.THREE: # Employees
            self.employee_menu.get_manager_employees_menu()
             #name = input("name")
            #ssn = input("ssn")
            #input("phone")
            #input("email")
            #logicwrapper.create_empl(Emplpoyee(name, ssn, ...))

        elif user_selection == self.const.FOUR: # Voyages
            self.voyage_menu.get_manager_voyage()

        elif user_selection == self.const.QUIT:
            print(self.const.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    
    def get_employee(self):
        pass
    

    def main(self):
        print(self.ascii_nanair)
        print(self.main_menu)
        print(self.main_menu_options)
        user_selection = self.input_prompt()

        if user_selection == self.const.ONE:
            self.get_manager()
        
        elif user_selection == self.const.TWO:
            self.get_shift_superviser()
        
        elif user_selection == self.const.THREE:
            self.get_employee()
