

class Desinations:
    def __init__(self, id, destination, numeric_id):
        self.id = id 
        self.destination = destination
        self.numeric_id = numeric_id

    def __str__(self):
        return f"Destination ID: {self.id}, Name of destination: {self.destination}, Destination numeric ID: {self.numeric_id}"
    