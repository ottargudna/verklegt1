from Model.airplane import Airplane
from data_layer.data_wrapper import Data_Wrapper

class Airplane_Logic:
    def __init__(self, data_connection) -> None:
        self.datawrapper = data_connection

    def create_airplane(self, airplane):
        """Takes in airplane object and forwards it to the data layer"""
        check_existing_airplanes = self.airplane_already_exist(airplane)
        if check_existing_airplanes == False:
            self.data_wrapper.create_airplane(airplane)
        else:
            return False
        #if false enter another name

    def get_all_airplanes(self):
        """Gets all airplane"""
        self.data_wrapper.get_all_airplanes()

    def airplane_already_exist(self, airplane):
        every_airplane = self.datawrapper.get_all_airplanes()
        for plane in every_airplane:
            if airplane[0] == plane.plane_insignia:
                return True # already exists
        
