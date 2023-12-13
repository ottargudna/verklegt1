#from Model.desinations import Desinations
import UI_layer.constants
#import string


#BORDER = 109 * "="
#QUIT = "q"
#BACK = "b"
#EXIT_TEXT = "Goodbye :)"
#SELECTION_ONE = "1"
#SELECTION_TWO = "2"
#SELECTION_THREE = "3"
#SELECTION_FOUR = "4"
#SELECTION_FIVE = "5"


class Destiantions_menu_ui:

    def __init__(self) -> None:
        self.constants = UI_layer.constants
        self.manager_menu = f"""
                                [{self.constants.SELECTION_ONE}] Register a new destination
                                [{self.constants.SELECTION_TWO}] Edit destinations
                                [{self.constants.SELECTION_THREE}] List all destinations
{self.constants.BORDER}
        """
    
    def get_manager_destinations(self):
        print(self.constants.ASCII_NANAIR)
        print(self.manager_menu)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # Register a new destination
            self.register_new_destination()
        
        elif user_selection == self.constants.SELECTION_TWO: # Edit destinations
            self.edit_destanation()

        elif user_selection == self.constants.SELECTION_THREE: # List all destinations
            self.list_all_destinations()

        elif user_selection == self.constants.QUIT:
            print(self.constants.EXIT_TEXT)
            quit()
    
        else: # Go back
            pass
    
    def register_new_destination(self):
        pass

    def edit_destanation(self):
        pass

    def list_all_destinations(self):
        pass
