

from data_layer.data_wrapper import Data_Wrapper
from logic_layer.airplane_logic import Airplane_Logic
from logic_layer.destinations_logic import Destinations_Logic
from logic_layer.employee_logic import Employee_Logic
from logic_layer.flights_logic import Flights_Logic
from logic_layer.voyage_logic import Voyage_Logic


class Logic_Wrapper:
    def __init__(self) -> None:
        self.data_wrapper = Data_Wrapper
        self.employee_logic = Employee_Logic(self.data_wrapper)
        self.airplane_logic = Airplane_Logic(self.data_wrapper)
        self.destination_logic = Destinations_Logic(self.data_wrapper)
        self.flight_logic = Flights_Logic(self.data_wrapper)
        self.voyage = Voyage_Logic(self.data_wrapper)


    """Hérna á að koma öll föll sem eru notuð og returna þeim"""
