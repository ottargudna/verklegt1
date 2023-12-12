from Model.flights import Flights

BORDER = 109 * "*"

class Flights_menu_ui:

    def __init__(self) -> None:
        self.main_menu = f"""
                                [1] 
                                [2] 
                                [3] 
                                [4] 
{BORDER}
        """

    def input_prompt(self):
        return input("Enter your selection: ")
    
    def print_menu():
        pass