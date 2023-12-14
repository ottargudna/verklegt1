
class Voyage:
    def __init__(self, voyage_number, dep_from, arr_at, aircraft_id, date_out, date_home, captain, copilot, flight_service_manager, flight_attendant1, flight_attendant2):
        self.voyage_number = voyage_number
        self.dep_from = dep_from
        self.arr_at = arr_at
        self.aircraft_id = aircraft_id
        self.date_out = date_out
        self.date_home = date_home
        self.captain = captain
        self.copilot = copilot
        self.flight_service_manager = flight_service_manager
        self.flight_attendant1 = flight_attendant1
        self.flight_attendant2 = flight_attendant2
    

    def __str__(self) -> str:
        return f"Voyage_number: {self.voyage_number}, Departure from: {self.dep_from}, Arriving at: {self.arr_at}, Aircraft ID: {self.aircraft_id}, Date flying out: {self.date_out}, Date flying home: {self.date_home}, Captain: {self.catain}, Copilot: {self.copilot}, Flight service manager: {self.flight_service_maneger}, Flight attendents: {self.flight_attendant1} and {self.flight_attendant2}"