
#destination,airport_intials,flight_time,distance_from_iceland
class Desinations:
    def __init__(self, destination, airport_intials, flight_time, distance_from_iceland):
        self.destination = destination
        self.airport_intials = airport_intials
        self.flight_time = flight_time
        self.distance_from_iceland = distance_from_iceland

    def __str__(self):
        return f"Destination: {self.destination}, Airport intials: {self.airport_intials}, Estimated flight time: {self.flight_time}, Distance from Iceland: {self.distance_from_iceland}"
    