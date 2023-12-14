from Model.airplane import Airplane
from logic_layer.logic_wrapper import Logic_Wrapper
import UI_layer.constants



class Airplane_menu_ui:

    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()
        self.const = UI_layer.constants

    def get_manager_airplane_menu(self):
        """ """
        print(self.const.airplane_menu())
        user_selection = self.const.input_selection()

        if user_selection == self.const.ONE: # Register airplane
            self.get_register_airplane()

        elif user_selection == self.const.TWO: # Edit airplane
            self.get_list_airplanes()

        elif user_selection == self.const.QUIT:
            print(self.const.EXIT_TEXT)
            quit()
        
        else: # Go back
            pass
    
    def get_register_airplane(self):

        insignia = input("Enter plane insignia: ")
        plane_id = input("Enter the plane id: ")
        seats = input("Enter the number of seats: ")
        airplane = Airplane(insignia, plane_id, seats)
        register_airplane = self.logic_wrapper.create_airplane(airplane)
        return register_airplane

    def get_list_airplanes(self):
        airplanes = self.logic_wrapper.get_all_airplanes()
        print(Airplane(airplanes))
    
    
