from Model.flights import Flights

class Flights_Logic:

    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def destination(self, flight):        
        self.data_wrapper.destination(flight)

    def register_flight(self):
        self.data_wrapper.register_flight()
        
    def get_flight_details(self, flight):
        self.data_wrapper.get_flight_details(flight)
        
    def departure_time(self):
        self.data_wrapper.departure_time.

    def flight_status(self):
        self.data_wrapper.
    
    def create_flight(self):
        self.data_wrapper.

    def get_all_flights(self):
        return self.data_wrapper.get_all_fligths()