from Model.voyage import Voyage

BORDER = 109 * "*"

class Voyage_menu_ui:

    def __init__(self) -> None:
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

    def staff_member_menu(self) -> None:
        print(BORDER)
        print("")
        print("[1] ")
        print("[2] ")
        print("[3] ")
        print()
        print("[B]ack to main menu  [Q]uit")
        print(BORDER)

        self.input_prompt(self)
    
    def input_prompt(self):
        return input("Enter your selection: ")