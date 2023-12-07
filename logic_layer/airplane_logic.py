from Model.airplane import Airplane
from data_layer.data_wrapper import Data_Wrapper

class Airplane_Logic:
    def __init__(self, data_connection) -> None:
        self.datawrapper = data_connection

    def register_airplane(self, airplane):
        """Takes in airplane object and forwards it to the data layer"""
        self.data_wrapper.create_airplane(airplane)

    def get_all_airplanes(self):
        """Gets all airplane"""
        self.data_wrapper.get_all_airplanes()
    
    def edit_airplane(self, airplane):
        '''Takes in name of an airplane and forwards it to data layer'''
        self.data_wrapper.edit_airplane(airplane)

    def list_airplanes(self):
        pass

    def validate_airplane(self):
        pass