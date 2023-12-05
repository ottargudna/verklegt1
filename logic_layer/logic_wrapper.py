

from logic_layer.airplane_logic import Airplane_Logic
from logic_layer.destinations_logic import Destinations_Logic
from logic_layer.employee_logic import Employee_Logic
from logic_layer.flights_logic import Flights_Logic
from logic_layer.voyage_logic import Voyage_Logic


class Logic_Wrapper:
    def __init__(self) -> None:
        self.employee_logic = Employee_Logic
        self.airplane_logic = Airplane_Logic
        self.destination_logic = Destinations_Logic
        self.flight_logic = Flights_Logic
        self.voyage = Voyage_Logic


    """Hérna á að koma öll föll sem eru notuð og returna þeim"""
