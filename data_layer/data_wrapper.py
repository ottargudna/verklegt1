
from data_layer.Airplane_Data import Airplane_Data
from data_layer.Destinations_Data import Destinations_Data
from data_layer.Employee_Data import Employee_Data
from data_layer.Flights_Data import Flights_Data
from data_layer.Voyage_Data import Voyage_Data


class Data_Wrapper:
    def __init__(self) -> None:
        self.employee_data = Employee_Data()
        self.airplane_data = Airplane_Data()
        self.destination_data = Destinations_Data()
        self.flight_data = Flights_Data()
        self.voyage_data= Voyage_Data()

    def get_all_employees(self):
        return self.employee_data.get_all_employees()
    
    def create_employees(self):
        return self.employee_data.create_employee()
    
    def get_all_destinations(self):
        return self.destination_data.get_all_destinations()

    def create_destination(self):
        return self.destination_data.create_destination()

    def get_all_voyages(self):
        return self.voyage_data.get_all_voyages()
    
    def create_voyages(self):
        return self.voyage_data.create_voyage()
    
    def get_all_airplanes(self):
        return self.airplane_data.get_all_airplanes()
    
    def create_airplane(self):
        return self.airplane_data.create_airplane()
    

    
