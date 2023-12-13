from Model.airplane import Airplane
from UI_layer.mainmenu_ui import MainMenu_ui
from logic_layer.logic_wrapper import Logic_Wrapper


BORDER = 109 * "*"
QUIT = "q"
BACK = "b"
EXIT_TEXT = "Goodbye :)"
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"


class Airplane_menu_ui:

    def __init__(self):
        self.main_menu = MainMenu_ui()
        self.logic_wrapper = Logic_Wrapper()

        self.manager_menu = f"""
                                [{SELECTION_ONE}] Register airplane
                                [{SELECTION_TWO}] Edit airplane
{BORDER}
        """

    def get_manager_airplane_menu(self):
        print(self.main_menu.ascii_nanair)
        print(self.manager_menu)
        print(self.main_menu.options)
        user_selection = self.main_menu.input_prompt()

        if user_selection == SELECTION_ONE: # Register airplane
            self.get_register_airplane()

        elif user_selection == SELECTION_TWO: # Edit airplane
            self.get_edit_airplane()

        elif user_selection == QUIT:
            print(EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    
    def get_register_airplane(self):
        pass

    def get_edit_airplane(self):
        pass
