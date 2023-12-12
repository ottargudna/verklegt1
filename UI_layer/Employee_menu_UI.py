from Model.employee import Employee


BORDER = 109 * "*"
SELECTION_ONE = "1"
SELECTION_TWO = "2"
SELECTION_THREE = "3"
SELECTION_FOUR = "4"
SELECTION_FIVE = "5"


class Employee_menu_ui:

    def __init__(self) -> None:
        self.main_menu = f"""
                                [1] List all employees
                                [2] Pilot
                                [3] Crew
        {BORDER}
        """

        self.pilot_menu = f"""
                                [{SELECTION_ONE}] Register a new pilot
                                [{SELECTION_TWO}] Edit information of a pilot
                                [{SELECTION_THREE}] Search for a pilot
                                [{SELECTION_FOUR}] List pilots
{BORDER}
        """
        self.crew = f"""
                                [{SELECTION_ONE}] Register a new crew member
                                [{SELECTION_TWO}] Edit information of a crew member
                                [{SELECTION_THREE}] Search for a crew member
                                [{SELECTION_FOUR}] List all crew members
{BORDER}
        """

