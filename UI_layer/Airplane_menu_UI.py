from Model.airplane import Airplane

class Airplane_menu_ui:

    def __init__(self, name, type, manifacturer, seats) -> None:
        self.name = name
        self.type = type
        self.manifacturer = manifacturer
        self.seats = seats