

#from data_layer.data_wrapper import Data_Wrapper
from logic_layer.airplane_logic import Airplane_Logic
from logic_layer.destinations_logic import Destinations_Logic
from logic_layer.employee_logic import Employee_Logic
from logic_layer.flights_logic import Flights_Logic
from logic_layer.voyage_logic import Voyage_Logic


class Logic_Wrapper:
    def __init__(self) -> None:
        #self.data_wrapper = Data_Wrapper
        self.employee_logic = Employee_Logic(self.data_wrapper)
        self.airplane_logic = Airplane_Logic(self.data_wrapper)
        self.destination_logic = Destinations_Logic(self.data_wrapper)
        self.flight_logic = Flights_Logic(self.data_wrapper)
        self.voyage = Voyage_Logic(self.data_wrapper)


    """Here comes all functions sem that are used in the logic layer and returns them"""

    #Employees
    def create_employee(self, employee):
        self.employee_logic.create_employee(employee)

    def get_all_employees(self):
        self.employee_logic.get_all_employees()

    def edit_employee(self, employee):
        self.employee_logic.edit_employee(employee)

    #Airplane
    def create_airplane(self, airplane):
        self.airplane_logic.create_airplane(airplane)

    def get_all_airplanes(self):
        self.airplane_logic.get_all_airplanes()

    #Destinations

    def create_destination(self, destination):
        """Takes in destination object and forwards it to the data layer"""
        self.destination_logic.create_destination(destination)

    def get_all_destinations(self):
        """Gets all destinations"""
        self.destination_logic.get_all_destinations()
        
    #Voyage
    def get_all_voyages(self):
        self.voyage_logic.get_all_voyages()

    def create_voyage(self, voyage):
        """Takes in voyage object and forwards it to the data layer"""
        self.voyage_logic.create_voyage(voyage)





