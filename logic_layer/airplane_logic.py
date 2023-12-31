#from Model.airplane import Airplane
from data_layer.data_wrapper import Data_Wrapper

class Airplane_Logic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
        self.datawrapper = Data_Wrapper()

    def create_airplane(self, airplane):
        """Takes in airplane object and forwards it to the data layer"""
        check_existing_airplanes = self.airplane_already_exist(airplane)

        if check_existing_airplanes == False:
            return self.datawrapper.create_airplane(airplane)
        else:
            return False

    def get_all_airplanes(self):
        """Gets all airplanes"""
        return self.datawrapper.get_all_airplanes()

    def airplane_already_exist(self, airplane):
        every_airplane = self.datawrapper.get_all_airplanes()

        every_id = []

        for id in every_airplane:
            every_id.append(id.aircraft_id)


       
        if airplane.aircraft_id in every_id:
            return True # already exists
        else:
            return False

        
