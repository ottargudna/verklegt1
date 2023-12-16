from Model.desinations import Desinations
import UI_layer.constants
from logic_layer.logic_wrapper import Logic_Wrapper
from UI_layer.input_validate import Validate

class Destiantions_menu_ui:

    def __init__(self) -> None:
        self.const = UI_layer.constants
        self.logic_wrapper = Logic_Wrapper()
        self.model = Desinations
        self.input_validate = Validate()
    
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

        dest_name = input("Enter the country: ").lower()
        while self.input_validate.validate_name(dest_name) == False:
            print("Invalid country, please try again")
            dest_name = input("Enter the country: ").lower()

        airport = input("Enter the initials of the airport (3 letters): ").upper()
        while self.input_validate.dest_intials(airport) == False:
            print("Invalid initials, please try again")
            airport = input("Enter the initials of the airport (3 letters): ").upper()

        flight_time = input("Enter the flight time (in hours): ")
        while self.input_validate.flight_time_and_distance(flight_time) == False:
            print("Invalid flight time, please try again")
            flight_time = input("Enter the flight time (in hours): ")

        distance = input("Enter the distance from Iceland: ")
        while self.input_validate.flight_time_and_distance(distance) == False:
            print("Invalid distance, please try again")
            distance = input("Enter the distance from Iceland: ")

        contact_name = input("Enter the contact name: ").lower()
        while self.input_validate.validate_name(contact_name) == False:
            print("Invalid name, please try again")
            contact_name = input("Enter the contact name: ").lower()
        
        contact_number = input("Enter the contact emergency number: ")
        while self.input_validate.validate_phone_number(contact_number) == False:
            print("Invalid emergency number, please try again")
            contact_number = input("Enter the contact emergency number: ")

        destination = Desinations(dest_name, airport, flight_time, distance, contact_name, contact_number)
        register_destination = self.logic_wrapper.create_destination(destination)
        
        print("Destination has been registered")
        input("Press ENTER to go back to the menu: ")
        return register_destination

    def update_destination(self):
        """Gets information from user to send to logic layer to edit information on a destinations"""

        d = Desinations
        d.destination  = input("What destination would you like to edit?: ").lower()
        
        d.contact_name = input("Enter the contact name: ").lower()
        d.emergency_phone_nr = input("Enter the contact emergency number: ")

        updated_destination = self.logic_wrapper.update_destination(d)
        return updated_destination

    def list_all_destinations(self):
        """Gets a list from the logic layer and prints it out"""

        all_destinations = self.logic_wrapper.get_all_destinations()
        for destination in all_destinations:
            print(f"Destination: {destination.destination:<10} {destination.airport_initials:<10}   flight time: {destination.flight_time:<3}")
        input("Press ENTER to go back to the menu: ")
