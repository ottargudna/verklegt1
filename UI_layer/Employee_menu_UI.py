from Model.employee import Employee

BORDER = 109 * "*"

class Employee_menu_ui:

    def __init__(self) -> None:
        self.employee_menu = f"""
        [1] Pilot and Crew
        [2] Pilot
        [3] Crew
        {BORDER}
        """

        self.pilot_crew_menu = """
        
        """

        self.main_menu = f"""
                                [1] List of flights to specific destinations
                                [2] List of the most popular destinations
                                [3] Register a new destination
                                [4] Edit destinations
{BORDER}
        """

        self.options = f"""
                                [B]ack to main menu     [Q]uit
{BORDER}
        """

        self.ascii_nanair = f"""
{BORDER}
                              _    _          _    _       __     _____  _____
                __|__        |  \ | |   __ _ |  \ | |     /  \   |_   _||  _  \         __|__ 
            ---o-(_)-o---    |   \| | / __' ||   \| |    / /\ \    | |  | |_|  |    ---o-(_)-o---
                             | |\   || |__| || |\   |   /  __  \  _| |_ |  _ _/      
                             |_| \__| \___,_||_| \__|  /__/  \__\|_____||_| \_\ 
{BORDER}
        """
    
    def menu_output(self):
        print(BORDER)
        print("[1] Pilot and Crew")
        print("[2] Pilot")
        print("[3] Crew")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(BORDER)

        self.input_prompt()

    def input_prompt(self):
        return input("Enter your selection: ")
    
    def pilot_menu(self):
        print(BORDER)
        print("[1] Register a new pilot")
        print("[2] Edit information of a pilot")
        print("[3] Search for a pilot")
        print("[4] List pilots")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(BORDER)
    
