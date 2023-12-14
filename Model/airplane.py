

class Airplane:
    def __init__(self, aircraft_id, plane_type_id, capacity):
        self.aircraft_id = aircraft_id
        self.plane_type_id = plane_type_id
        self.capacity = capacity

    def __str__(self):
        return f"Plane insignia: {self.aircraft_id}, Plane type ID: {self.plane_type_id}, Capacity: {self.capacity}"