'''
from Model.flights import Flights

BORDER = 109 * "*"

class Flights_menu_ui:

    def __init__(self) -> None:
        self.main_menu = f"""
                                [1] 
                                [2] 
                                [3] 
                                [4] 
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

    def input_prompt(self):
        return input("Enter your selection: ")
    
    def print_menu():
        pass

'''