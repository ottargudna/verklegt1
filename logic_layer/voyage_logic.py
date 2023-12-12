from Model.voyage import Voyage
from logic_layer.flights_logic import Flights

class Voyage_Logic:
    
    def __init__(self) -> None:
        pass

    def create_voyage(self, voyage):
        """Takes in destination object and forwards it to the data layer"""
        self.data_wrapper.create_voyage(voyage)


    def schedule_voyage(self):
        pass

    def get_all_voyages(self):
        self.data_wrapper.get_all_voyages()


    