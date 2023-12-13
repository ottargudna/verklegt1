
#destination,airport_intials,flight_time,distance_from_iceland
class Desinations:
    def __init__(self, destination, airport_intials, flight_time, distance_from_iceland, contact_name, emergency_phone_nr):
        self.destination = destination
        self.airport_initials = airport_intials
        self.flight_time = flight_time
        self.distance_from_iceland = distance_from_iceland
        self.contact_name = contact_name
        self.emergency_phone_nr = emergency_phone_nr

    def __str__(self):
        return f"Destination: {self.destination}, Airport initials: {self.airport_initials}, Estimated flight time: {self.flight_time}, Distance from Iceland: {self.distance_from_iceland}, contact_name: {self.contact_name}, emergency_phone_nr: {self.emergency_phone_nr}"
    