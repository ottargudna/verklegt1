#from Model.voyage import Voyage
import UI_layer.constants

#BORDER = 109 * "*"
#QUIT = "q"
#BACK = "b"
#SELECTION_ONE = "1"
#SELECTION_TWO = "2"
#SELECTION_THREE = "3"
#SELECTION_FOUR = "4"
#SELECTION_FIVE = "5"


class Voyage_menu_ui:

    def __init__(self) -> None:
        #self.main_menu = MainMenu_ui()
        self.constants = UI_layer.constants
        self.voyage_menu_manager = f"""
                                [{self.constants.SELECTION_ONE}] Register a new voyage
                                [{self.constants.SELECTION_TWO}] List all voyages
                                [{self.constants.SELECTION_THREE}] List all voyages for a given day
                                [{self.constants.SELECTION_FOUR}] List all voyages for a given week
                                [{self.constants.SELECTION_FIVE}] List all voyages of a staff member for a given week
{self.constants.BORDER}
        """
        
        self.voyage_menu_shift_superviser = f"""
                                [{self.constants.SELECTION_ONE}] List all voyages
                                [{self.constants.SELECTION_TWO}] List all voyages for a given day
                                [{self.constants.SELECTION_THREE}] List all voyages for a given week
                                [{self.constants.SELECTION_FOUR}] List all voyages of a staff member for a given week
{self.constants.BORDER}
        """


    def get_manager_voyage(self):
        print(self.constants.ASCII_NANAIR)
        print(self.voyage_menu_manager)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # Register a new voyage
            self.get_register_new_voyage()

        elif user_selection == self.constants.SELECTION_TWO: # List all voyages
            self.get_list_all_voyages()

        elif user_selection == self.constants.SELECTION_THREE: # List all voyages for a given day
            self.get_list_voyages_for_day()

        elif user_selection == self.constants.SELECTION_FOUR: # List all voyages for a given week
            self.get_list_voyages_for_week

        elif user_selection == self.constants.SELECTION_FIVE: # List all voyages of a staff member for a given week
            self.get_list_voyages_of_employee()

    def get_shift_superviser_voyage(self):
        print(self.constants.ASCII_NANAIR)
        print(self.voyage_menu_shift_superviser)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # List all voyages
            self.get_list_all_voyages()

        elif user_selection == self.constants.SELECTION_TWO: # List all voyages for a given day
            self.get_list_voyages_for_day()

        elif user_selection == self.constants.SELECTION_THREE: # List all voyages for a given week
            self.get_list_voyages_for_week()

        elif user_selection == self.constants.SELECTION_FOUR: # List all voyages of a staff member for a given week
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
