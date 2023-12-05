from Model.desinations import Desinations

STARS = 50 * "*"

class Destiantions_menu_ui:

    def __init__(self) -> None:
        pass

    def menu_output(self):
        print(STARS)
        print("[1] List of flights to specific destinations")
        print("[2] List of the most popular destinations")
        print("[3] Register a new destination")
        print("[4] Edit destinations")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(STARS)

        self.input_prompt()

    def input_prompt(self):
        return input("Enter your selection: ")