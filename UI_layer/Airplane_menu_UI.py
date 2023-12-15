from Model.airplane import Airplane
from logic_layer.logic_wrapper import Logic_Wrapper
import UI_layer.constants
from UI_layer.input_validate import Validate



class Airplane_menu_ui:

    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()
        self.input_validate = Validate()
        self.const = UI_layer.constants

    def get_manager_airplane_menu(self):
        """Prints out the choices for working with airplanes and calls functions accordingly"""
        user_selection = ""
        while user_selection != self.const.BACK:
            print(self.const.airplane_menu())
            user_selection = self.const.input_selection()

            if user_selection == self.const.ONE: # Register airplane
                self.get_register_airplane()

            elif user_selection == self.const.TWO: # Edit airplane
                self.get_list_airplanes()

            elif user_selection == self.const.QUIT:
                print(self.const.EXIT_TEXT)
                quit()
            
    
    def get_register_airplane(self):

        a = Airplane

        plane_id = input("Enter the plane ID: ")
        while self.input_validate.aircraft_id(plane_id) == False:
            print("Invalid plane ID, please try again")
            plane_id = input("Enter the plane ID: ")
        a.aircraft_id = plane_id

        plane_type = input("Enter plane type: ")
        while self.input_validate.airplane_type(plane_type) == False:
            print("Invalid insignia, please try again")
            plane_type = input("Enter plane type: ")
        a.plane_type_id = plane_type
        

        seats = input("Enter the number of seats: ")
        while self.input_validate.validate_seats(seats) == False:
            print("Invalid seats, please try again")
            seats = input("Enter the number of seats: ")
        a.capacity = seats
        register_airplane = self.logic_wrapper.create_airplane(a)
        print("Airplane has been registered")
        input("Press ENTER to go back to the menu: ")

        return register_airplane

    def get_list_airplanes(self):
        airplanes = self.logic_wrapper.get_all_airplanes()
        for airplane in airplanes:
            print(airplane)
        input("Press ENTER to go back to the menu: ")
    