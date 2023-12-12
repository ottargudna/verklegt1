from Model.voyage import Voyage

BORDER = 109 * "*"
QUIT = "q"
BACK = "b"
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"


class Voyage_menu_ui:

    def __init__(self) -> None:
        self.voyage_menu_manager = f"""
                                [{SELECTION_ONE}] Register a new voyage
                                [{SELECTION_TWO}] List all voyages
                                [{SELECTION_THREE}] List all voyages for a given day
                                [{SELECTION_FOUR}] List all voyages for a given week
                                [{SELECTION_FIVE}] List all voyages of a staff member for a given week
{BORDER}
    """ 
