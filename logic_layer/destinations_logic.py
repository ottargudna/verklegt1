

from Model.desinations import Desinations

class Destinations_Logic:
    def __init__(self) -> None:
        pass

    def create_destination(self, destination):
        """Takes in destination object and forwards it to the data layer"""
        self.data_wrapper.create_destination(destination)


    def get_all_destinations(self):
        """Gets all destinations"""
        self.data_wrapper.get_all_destinations()

    #def edit_destanations(self):
        '''Takes in name of an destination and forwards it to data layer'''
       # self.data_wrapper.edit_destinations()