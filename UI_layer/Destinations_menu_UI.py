from Model.desinations import Desinations
from UI_layer.mainmenu_ui import MainMenu_ui
import string


BORDER = 109 * "="
QUIT = "q"
BACK = "b"
EXIT_TEXT = "Goodbye :)"
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"


class Destiantions_menu_ui:

    def __init__(self) -> None:
        self.main_menu = MainMenu_ui()
        self.manager_menu = f"""
                                [{SELECTION_ONE}] Register a new destination
                                [{SELECTION_TWO}] Edit destinations
                                [{SELECTION_THREE}] List all destinations
{BORDER}
        """
    
    def get_manager_destinations(self):
        print(self.main_menu.ascii_nanair)
        print(self.manager_menu)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == SELECTION_ONE: # Register a new destination
            self.register_new_destination()
        
        elif user_selection == SELECTION_TWO: # Edit destinations
            self.edit_destanation()

        elif user_selection == SELECTION_THREE: # List all destinations
            self.list_all_destinations()

        elif user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
    
        else: # Go back
            pass
    
    def register_new_destination(self):
        pass

    def edit_destanation(self):
        pass

    def list_all_destinations(self):
        pass
