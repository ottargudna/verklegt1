from Model.voyage import Voyage
from UI_layer.mainmenu_ui import MainMenu_ui

BORDER = 109 * "*"
QUIT = "q"
BACK = "b"
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"


class Voyage_menu_ui:

    def __init__(self) -> None:
        self.main_menu = MainMenu_ui()
        self.voyage_menu_manager = f"""
                                [{SELECTION_ONE}] Register a new voyage
                                [{SELECTION_TWO}] List all voyages
                                [{SELECTION_THREE}] List all voyages for a given day
                                [{SELECTION_FOUR}] List all voyages for a given week
                                [{SELECTION_FIVE}] List all voyages of a staff member for a given week
{BORDER}
        """
        
        self.voyage_menu_shift_superviser = f"""
                                [{SELECTION_ONE}] List all voyages
                                [{SELECTION_TWO}] List all voyages for a given day
                                [{SELECTION_THREE}] List all voyages for a given week
                                [{SELECTION_FOUR}] List all voyages of a staff member for a given week
{BORDER}
        """


    def get_manager_voyage(self):
        print(self.main_menu.ascii_nanair)
        print(self.voyage_menu_manager)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == SELECTION_ONE: # Register a new voyage
            self.get_register_new_voyage()

        elif user_selection == SELECTION_TWO: # List all voyages
            self.get_list_all_voyages()

        elif user_selection == SELECTION_THREE: # List all voyages for a given day
            self.get_list_voyages_for_day()

        elif user_selection == SELECTION_FOUR: # List all voyages for a given week
            self.get_list_voyages_for_week

        elif user_selection == SELECTION_FIVE: # List all voyages of a staff member for a given week
            self.get_list_voyages_of_employee()

    def get_shift_superviser_voyage(self):
        print(self.main_menu.ascii_nanair)
        print(self.voyage_menu_shift_superviser)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == SELECTION_ONE: # List all voyages
            self.get_list_all_voyages()

        elif user_selection == SELECTION_TWO: # List all voyages for a given day
            self.get_list_voyages_for_day()

        elif user_selection == SELECTION_THREE: # List all voyages for a given week
            self.get_list_voyages_for_week()

        elif user_selection == SELECTION_FOUR: # List all voyages of a staff member for a given week
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
