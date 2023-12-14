#from Model.airplane import Airplane
from data_layer.data_wrapper import Data_Wrapper

class Airplane_Logic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
        self.datawrapper = Data_Wrapper()

    def create_airplane(self, airplane):
        """Takes in airplane object and forwards it to the data layer"""
        check_existing_airplanes = self.airplane_already_exist(airplane)
        if check_existing_airplanes == True:
        if check_existing_airplanes == False:
            self.datawrapper.create_airplane(airplane)
        else:
            return False
        else:
            self.data_wrapper.create_airplane(airplane)
        #if true enter another name and return a str try another name

    def get_all_airplanes(self):
        """Gets all airplanes"""
        self.datawrapper.get_all_airplanes()

    def airplane_already_exist(self, airplane):
        every_airplane = self.datawrapper.get_all_airplanes()
        """Gets all airplane"""
        self.datawrapper.create_airplane(airplane)
        #if true enter another name and return a str try another name

    def get_all_airplanes(self):
        """Gets all airplanes"""
        self.datawrapper.get_all_airplanes()

    def airplane_already_exist(self, airplane):
        every_airplane = self.datawrapper.get_all_airplanes()

        for plane in every_airplane:
            if airplane.plane_insignia == plane.plane_insignia:
                return True # already exists
        
