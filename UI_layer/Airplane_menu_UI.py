from Model.airplane import Airplane
from logic_layer.logic_wrapper import Logic_Wrapper
from UI_layer import constants


class Airplane_menu_ui:

    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

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
