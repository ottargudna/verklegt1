from Model.airplane import Airplane
from logic_layer.logic_wrapper import Logic_Wrapper


BORDER = 109 * "*"
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"


class Airplane_menu_ui:

    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

        self.manager_menu = f"""
                                [{SELECTION_ONE}] Register airplane
                                [{SELECTION_TWO}] Edit airplane
{BORDER}
        """
