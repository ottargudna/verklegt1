<<<<<<< Updated upstream
import pyfiglet as pfg
=======
>>>>>>> Stashed changes
from Model.desinations import Desinations
import string


BORDER = 109 * "="
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"


class Destiantions_menu_ui:

    def __init__(self) -> None:
        self.main_menu = f"""
                                [{SELECTION_ONE}] Register a new destination
                                [{SELECTION_TWO}] Edit destinations
                                [{SELECTION_THREE}] List all destinations
{BORDER}
        """


    def input_prompt(self):
        return input("Enter your selection: ")
