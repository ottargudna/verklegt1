from Model.desinations import Desinations
import UI_layer.constants
from logic_layer.logic_wrapper import Logic_Wrapper

class Destiantions_menu_ui:

    def __init__(self) -> None:
        self.const = UI_layer.constants
        self.logic_wrapper = Logic_Wrapper()
    
    def get_manager_destinations(self):
        """Prints out menues of options for the user and calls functions that go with them"""

        user_selection = ""
        while user_selection != self.const.BACK:
            print(self.const.destinations_menu())
            user_selection = self.const.input_selection()

            if user_selection == self.const.ONE: # Register a new destination
                self.register_new_destination()
            
            elif user_selection == self.const.TWO: # Edit destinations
                self.update_destination()

            elif user_selection == self.const.THREE: # List all destinations
                self.list_all_destinations()

            elif user_selection == self.const.QUIT:
                print(self.const.EXIT_TEXT)
                quit()

    
    def register_new_destination(self):
        """Gets input from user and gets a function from the logic layer"""

        register_destination = False
        while register_destination == False:
            dest_name = input("Enter the country: ")
            airport = input("Enter the initials of the airport: ")
            flight_time = input("Enter the flight time: ")
            distance = input("Enter the distance from Iceland: ")
            contact_name = input("Enter the contact name: ")
            contact_number = input("Enter the contact emergency number: ")

            destination = Desinations(dest_name, airport, flight_time, distance, contact_name, contact_number)
            register_destination = self.logic_wrapper.create_destination(destination)
        return register_destination

    def update_destination(self):
        destination = input("What destination would you like to edit?: ").lower()
        update_dest = self.logic_wrapper.update_destination(destination)
        contact = input("Enter the contact name: ")
        emergency_num = input("Enter the contact emergency number: ")
        updated_destination = Desinations(contact, emergency_num)
        return updated_destination

    def list_all_destinations(self):
        """Gets a list from the logic layer and prints it out"""

        all_destinations = self.logic_wrapper.get_all_destinations()
        for destination in all_destinations:
            print(destination)
        input("Press ENTER to go back to the menu: ")
