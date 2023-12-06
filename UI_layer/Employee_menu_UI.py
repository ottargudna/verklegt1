from Model.employee import Employee

BORDER = 50 * "*"

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
    
