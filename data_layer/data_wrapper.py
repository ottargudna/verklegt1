

from data_layer.Airplane_Data import Airplane_Data
from data_layer.Destinations_Data import Destinations_Data
from data_layer.Employee_Data import Employee_Data
from data_layer.Flights_Data import Flights_Data
from data_layer.Voyage_Data import Voyage_Data


class Data_Wrapper:
    def __init__(self) -> None:
        self.employee_logic = Employee_Data
        self.airplane_logic = Airplane_Data
        self.destination_logic = Destinations_Data
        self.flight_logic = Flights_Data
        self.voyage = Voyage_Data


    """Hérna á að koma öll föll sem eru notuð og returna þeim"""
