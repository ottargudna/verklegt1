from Model.voyage import Voyage

STARS = 50 * "*"

class Voyage_menu_ui:

    def __init__(self) -> None:
        pass

    def staff_member_menu(self) -> None:
        print(STARS)
        print("")
        print("[1] ")
        print("[2] ")
        print("[3] ")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(STARS)

        self.input_prompt(self)
    
    def input_prompt(self):
        return input("Enter your selection: ")