
from data_layer.data_wrapper import Data_Wrapper
from Model.desinations import Desinations

class Destinations_Logic:

    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection
        self.datawrapper = Data_Wrapper()

    def create_destination(self, destination):
        """Takes in destination object and forwards it to the data layer"""
        every_destination = self.datawrapper.get_all_destinations()
        for d in every_destination:
            if destination == d:
                return False #already exists
        self.datawrapper.create_destination(destination)


    def get_all_destinations(self):
        """Gets all destinations"""
        self.datawrapper.get_all_destinations()

    def update_destination(self, destination):
        '''Takes in name of an destination and forwards it to data layer'''
        self.data_wrapper.update_destination(destination)