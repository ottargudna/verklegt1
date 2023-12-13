from Model.desinations import Desinations
import UI_layer.constants
from logic_layer.logic_wrapper import Logic_Wrapper
import string

class Destiantions_menu_ui:

    def __init__(self) -> None:
        self.const = UI_layer.constants
        self.logic_wrapper = Logic_Wrapper()
    
    def get_manager_destinations(self):
        print(self.const.destinations_menu)
        user_selection = self.const.input_selection()

        if user_selection == self.const.ONE: # Register a new destination
            self.register_new_destination()
        
        elif user_selection == self.const.TWO: # Edit destinations
            self.edit_destanation()

        elif user_selection == self.const.THREE: # List all destinations
            self.list_all_destinations()

        elif user_selection == self.const.QUIT:
            print(self.const.EXIT_TEXT)
            quit()
    
        else: # Go back
            pass
    
    def register_new_destination(self):
        destination_name = input("Enter the country: ")
        destination_airport = input("Enter the initials of the airport: ")
        destination_flight_time = input("Enter the flight time: ")
        destination_distance = input("Enter the distance from Iceland: ")
        destination_contact_name = input("Enter the contact name: ")
        destination_contact_nr = input("Enter the contact emergency number: ")

        destination = destination_name, destination_airport, destination_flight_time, destination_distance, destination_contact_name, destination_contact_nr
        return self.logic_wrapper.data_wrapper.create_destination(destination)

    def edit_destanation(self, destination):
        destination = input("What destination would you like to edit?: ")
        return self.logic_wrapper.edit_destanations(destination)

    def list_all_destinations(self):
        pass
