from Model.desinations import Desinations
import string

class Destiantions_menu_ui:

    def __init__(self) -> None:
        self.main_menu = MainMenu_ui()
    
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
