from Model.employee import Employee

STARS = 50 * "*"

class Employee_menu_ui:

    def __init__(self) -> None:
        pass    
    
    def menu_output(self):
        print(STARS)
        print("[1] Pilot and Crew")
        print("[2] Pilot")
        print("[3] Crew")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(STARS)

        self.input_prompt()

    def input_prompt(self):
        return input("Enter your selection: ")
    
    def pilot_menu(self):
        print(STARS)
        print("[1] Register a new pilot")
        print("[2] Edit information of a pilot")
        print("[3] Search for a pilot")
        print("[4] List pilots")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(STARS)
    
