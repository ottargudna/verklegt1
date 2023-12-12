import csv
from Model.desinations import Desinations

class Destinations_Data:
    def __init__(self) -> None:
        self.file_name = "Files/destinations.csv"

    def get_all_destinations(self):
        list = []
        with open(self.file_name, newline= '', encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list.append(Desinations(row["destination"], row ["airport"], row ["flight_time"], row["distance_from_iceland"]))
        return list 
    
    def create_destination(self, destination):
        with open(self.file_name, "a", newline= " ", encoding = " utf-8") as csvfile:
            fieldnames = ["destination", "airport", "flight_time", "distance_from_iceland"]
            writer = csv.DictReader(csvfile,fieldnames = fieldnames)
            writer.writerow({"destination": destination.destination, "airport": destination.airport, "flight_time": destination.flight_time, "distance_from_iceland": destination.distance_from_iceland,})