

class Airplane:
    def __init__(self, plane_insignia, plane_type_id, capacity):
        self.plane_insignia = plane_insignia
        self.plane_type_id = plane_type_id
        self.capacity = capacity

    def __str__(self):
        return f"Plane insignia: {self.plane_insignia}, Plane type ID: {self.plane_type_id}, Capacity: {self.capacity}"