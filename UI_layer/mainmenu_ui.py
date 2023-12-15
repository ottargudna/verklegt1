from UI_layer.Employee_menu_UI import Employee_menu_ui
from UI_layer.Destinations_menu_UI import Destiantions_menu_ui
from UI_layer.Airplane_menu_UI import Airplane_menu_ui
from UI_layer.Voyage_menu_UI import Voyage_menu_ui
import UI_layer.constants
from UI_layer.input_validate import Validate
from logic_layer.logic_wrapper import Logic_Wrapper

class MainMenu_ui:
    def __init__(self) -> None:
        self.employee_menu = Employee_menu_ui()
        self.destinations_menu = Destiantions_menu_ui()
        self.airplane_menu = Airplane_menu_ui()
        self.voyage_menu = Voyage_menu_ui()
        self.const = UI_layer.constants
        self.logic_wrapper = Logic_Wrapper()
        self.input_validate = Validate()
    
    
    def employee_name(self):
        return input("Enter your name: ")
    

    def get_shift_superviser(self):

        user_selection = ""
        while user_selection != self.const.BACK:
            print(self.const.shift_supervisor_menu())
            user_selection = self.const.input_selection()

            if user_selection == self.const.ONE: # List all Destinations
                self.destinations_menu.list_all_destinations()

            elif user_selection == self.const.TWO: # Employees
                self.employee_menu.get_employees_menu_shift_manager()

            elif user_selection == self.const.THREE: # Voyages
                self.voyage_menu.get_shift_superviser_voyage()
            
            elif user_selection == self.const.QUIT:
                print(self.const.EXIT_TEXT)
                quit()
        
    
    def get_manager(self):
        
        user_selection = ""
        while user_selection != self.const.BACK:
            print(self.const.manager_menu())
            user_selection = self.const.input_selection()

            if user_selection == self.const.ONE: # Airplanes
                self.airplane_menu.get_manager_airplane_menu()

            elif user_selection == self.const.TWO: # Destinations
                self.destinations_menu.get_manager_destinations()
                    
            elif user_selection == self.const.THREE: # Employees
                self.employee_menu.get_employees_manager()

            elif user_selection == self.const.FOUR: # Voyages
                self.voyage_menu.get_manager_voyage()

            elif user_selection == self.const.QUIT:
                print(self.const.EXIT_TEXT)
                quit()
        
    
    def get_employee(self):
        
        user_selection = ""
        while user_selection != self.const.BACK:
            print(self.const.employee_menu())
            user_selection = self.const.input_selection()

            if user_selection == self.const.QUIT:
                print(self.const.EXIT_TEXT)
                quit()

            elif user_selection == self.const.ONE: # Display Shifts
                shifts = self.display_shifts()
                if shifts == []:
                    print("Employee is not working here, please try again ")
                for shift in shifts:
                    print(f"date out: {shift.date_out:<10}   date home: {shift.date_home:<10}   dep from: {shift.dep_from:<3}   arr at: {shift.arr_at:<3}")

                input("Press ENTER to go back to menu: ")
    

    def display_shifts(self):
        ssn = input("SSN: ")
        while self.input_validate.validate_nid(ssn) == False:
            print("Invalid SSN, please try again")
            ssn = input("SSN: ")
        
        date = input("Enter date (YYYY.MM.DD): ")
        
        shifts = self.logic_wrapper.get_week_work(ssn, date)
        while shifts == False:
            print("Enter a valid date:")
            date = input("Enter date (YYYY.MM.DD): ")
            shifts = self.logic_wrapper.get_week_work(ssn, date)

        return shifts


    def main(self):
        print(self.const.main_menu())
        user_selection = self.const.input_selection()

        while True:
            if user_selection == self.const.QUIT:
                print(self.const.EXIT_TEXT)
                break

            if user_selection == self.const.ONE:
                self.get_manager()
            
            elif user_selection == self.const.TWO:
                self.get_shift_superviser()
            
            elif user_selection == self.const.THREE:
                self.get_employee()
