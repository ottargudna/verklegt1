from Model.voyage import Voyage
import UI_layer.constants
from logic_layer.logic_wrapper import Logic_Wrapper
import os

class Voyage_menu_ui:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper

    def __init__(self) -> None:
        self.const = UI_layer.constants
        self.logic_wrapper = Logic_Wrapper()

    def get_manager_voyage(self):
        print(self.const.voyage_menu_manager())
        user_selection = self.const.input_selection()

        if user_selection == self.const.ONE: # Register a new voyage
            self.get_register_new_voyage()

        elif user_selection == self.const.TWO: # List all voyages
            self.get_list_all_voyages()

        elif user_selection == self.const.THREE: # List all voyages for a given day
            self.get_list_voyages_for_day()

        elif user_selection == self.const.FOUR: # List all voyages for a given week
            self.get_list_voyages_for_week

        elif user_selection == self.const.FIVE: # List all voyages of a staff member for a given week
            self.get_list_voyages_of_employee()

    def get_shift_superviser_voyage(self):
        print(self.const.voyage_menu_shift_superviser())
        user_selection = self.const.input_selection()

        if user_selection == self.const.ONE: # List all voyages
            self.get_list_all_voyages()

        elif user_selection == self.const.TWO: # List all voyages for a given day
            self.get_list_voyages_for_day()

        elif user_selection == self.const.THREE: # List all voyages for a given week
            self.get_list_voyages_for_week()

        elif user_selection == self.const.FOUR: # List all voyages of a staff member for a given week
            self.get_list_voyages_of_employee()

    
    def get_register_new_voyage(self):
        departing_from = input("Departing from: ")
        arriving_at = input("Arriving at: ")
        aircraft_id = input("Aircraft ID: ")
        date_out = input("Date out: ")
        date_home = input("Date home: ")
        captain = input("Captain (press enter to leave empty): ")
        copilot = input("Copilot (press enter to leave empty): ")
        flight_service_manager = input("Flight service manager (press enter to leave empty): ")
        flight_attendant1 = input("Flight attendant (press enter to leave empty): ")
        flight_attendant2 = input("Flight attendant (press enter to leave empty): ")

        voyage = departing_from, arriving_at, aircraft_id, date_out, date_home, captain, copilot, flight_service_manager, flight_attendant1, flight_attendant2
        return self.logic_wrapper.create_voyage(voyage)

    def get_list_all_voyages(self):
        voyages = self.logic_wrapper.get_all_voyages()
        for voyage in voyages:
            if self.logic_wrapper.check_if_voyages_are_fully_staffed() == False:
                print(voyage.voyage_number, "Not staffed")

            else:
                print(voyage.voyage_number, "Fully staffed")
        input("Press ENTER to go back to the menu: ")

    def get_list_voyages_for_day(self):
        pass

    def get_list_voyages_for_week(self):
        pass

    def get_list_voyages_of_employee(self):
        pass
