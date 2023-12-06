import pyfiglet as pfg
from Model.desinations import Desinations
import string

BORDER = 109 * "="

class Destiantions_menu_ui:

    def __init__(self) -> None:
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

#         self.ascii_airplane = f"""
# {BORDER}
#                                                      |
#                                                      |
#                                                    .-'-.
#                                                   ' ___ '
#                                         ---------'  .-.  '---------
#                         _________________________'  '-'  '_________________________
#                          ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''
#                                        \    /  ||/   H   \||  \    /
#                                         '--'   OO   O|O   OO   '--'
#         """

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
    
    def print_menu(self) -> str:
        #print(self.ascii_airplane)
        print(self.ascii_nanair)
        print(self.main_menu)
        print(self.options)
        print()
        self.input_prompt()