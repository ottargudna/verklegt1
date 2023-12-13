#from Model.airplane import Airplane
import UI_layer.constants
#from logic_layer.logic_wrapper import Logic_Wrapper


#BORDER = 109 * "*"
#QUIT = "q"
#BACK = "b"
#EXIT_TEXT = "Goodbye :)"
#SELECTION_ONE = "1"
#SELECTION_TWO = "2"
#SELECTION_THREE = "3"
#SELECTION_FOUR = "4"
#SELECTION_FIVE = "5"


class Airplane_menu_ui:

    def __init__(self):
        #self.main_menu = MainMenu_ui()
        #self.logic_wrapper = Logic_Wrapper()
        self.constants = UI_layer.constants
        self.manager_menu = f"""
                                [{self.constants.SELECTION_ONE}] Register airplane
                                [{self.constants.SELECTION_TWO}] Edit airplane
{self.constants.BORDER}
        """

    def get_manager_airplane_menu(self):
        print(self.constants.ASCII_NANAIR)
        print(self.manager_menu)
        print(self.constants.OPTIONS)
        user_selection = self.constants.INPUT_PROMPT

        if user_selection == self.constants.SELECTION_ONE: # Register airplane
            self.get_register_airplane()

        elif user_selection == self.constants.SELECTION_TWO: # Edit airplane
            self.get_edit_airplane()

        elif user_selection == self.constants.QUIT:
            print(self.constants.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    
    def get_register_airplane(self):
        pass

    def get_edit_airplane(self):
        pass
