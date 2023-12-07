from Model.airplane import Airplane

BORDER = 109 * "*"

class Airplane_menu_ui:

    def __init__(self):

        self.ascii_nanair = f"""
{BORDER}
                              _    _          _    _       __     _____  _____
                __|__        |  \ | |   __ _ |  \ | |     /  \   |_   _||  _  \         __|__ 
            ---o-(_)-o---    |   \| | / __' ||   \| |    / /\ \    | |  | |_|  |    ---o-(_)-o---
                             | |\   || |__| || |\   |   /  __  \  _| |_ |  _ _/      
                             |_| \__| \___,_||_| \__|  /__/  \__\|_____||_| \_\ 
{BORDER}
        """

        self.manager_menu = f"""
                                [1] Register airplane
                                [2] Edit airplane
                                [3] List airplanes
{BORDER}
        """

        self.list_menu = f"""
                                [1] List all airplanes
                                [2] List airplanes after number of flights
                                [3] List airplanes after usage
{BORDER}
        """