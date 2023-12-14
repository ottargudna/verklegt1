from Model.desinations import Desinations
import UI_layer.constants
from logic_layer.logic_wrapper import Logic_Wrapper

class Destiantions_menu_ui:

    def __init__(self) -> None:
        self.const = UI_layer.constants
        self.logic_wrapper = Logic_Wrapper()
    
    def get_manager_destinations(self):
        print(self.const.destinations_menu())
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
        dest_name = input("Enter the country: ")
        airport = input("Enter the initials of the airport: ")
        flight_time = input("Enter the flight time: ")
        distance = input("Enter the distance from Iceland: ")
        contact_name = input("Enter the contact name: ")
        contact_number = input("Enter the contact emergency number: ")

        destination = dest_name, airport, flight_time, distance, contact_name, contact_number
        return self.logic_wrapper.data_wrapper.create_destination(destination)

    def edit_destanation(self, destination):
        destination = input("What destination would you like to edit?: ")
        return self.logic_wrapper.edit_destanations(destination)

    def list_all_destinations(self):
        all_destinations = self.logic_wrapper.get_all_destinations()
        for destination in all_destinations:
            print(destination)
