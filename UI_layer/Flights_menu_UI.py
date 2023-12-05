from Model.flights import Flights

STARS = 50 * "*"

class Flights_menu_ui:

    def __init__(self) -> None:
        pass

    def menu_output(self):
        print(STARS)
        print("[1] ")
        print("[2] ")
        print("[3] ")
        print("[4] ")
        print("[5] ")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(STARS)

        self.input_prompt()

    def input_prompt(self):
        return input("Enter your selection: ")