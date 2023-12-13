from Model.voyage import Voyage
import UI_layer.constants

class Voyage_menu_ui:

    def __init__(self) -> None:
        self.const = UI_layer.constants

    def get_manager_voyage(self):
        print(self.main_menu.ascii_nanair)
        print(self.voyage_menu_manager)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

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
        print(self.main_menu.ascii_nanair)
        print(self.voyage_menu_shift_superviser)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == self.const.ONE: # List all voyages
            self.get_list_all_voyages()

        elif user_selection == self.const.TWO: # List all voyages for a given day
            self.get_list_voyages_for_day()

        elif user_selection == self.const.THREE: # List all voyages for a given week
            self.get_list_voyages_for_week()

        elif user_selection == self.const.FOUR: # List all voyages of a staff member for a given week
            self.get_list_voyages_of_employee()

    
    def get_register_new_voyage(self):
        pass

    def get_list_all_voyages(self):
        pass

    def get_list_voyages_for_day(self):
        pass

    def get_list_voyages_for_week(self):
        pass

    def get_list_voyages_of_employee(self):
        pass
