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
                list.append(Desinations(row["destination"], row["airport_initials"], row["flight_time"], row["distance_from_iceland"], row["contact_name"], row["emergency_phone_nr"]))
        return list 
    
    def create_destination(self, destination):
        with open(self.file_name, "a", newline= " ", encoding = " utf-8") as csvfile:
            fieldnames = ["destination", "airport_initials", "flight_time", "distance_from_iceland", "contact_name", "emergency_phone_nr"]
            writer = csv.DictReader(csvfile,fieldnames = fieldnames)
            writer.writerow({"destination": destination.destination, "airport_initials": destination.airport_initials, "flight_time": destination.flight_time, "distance_from_iceland": destination.distance_from_iceland, "contact_name": destination.emergency_phone_nr})


    def update_destination(self, updated_destination):
        destinations = self.get_all_destination() 


        for destination in destinations: 
            if destination.destination == updated_destination.destination:
               #update contact name and emergency phone number
                destination.contact_name = updated_destination.contact_name
                destination.emergency_phone_nr = updated_destination.emergency_phone_nr

                with open(self.file_name, "w", newline = "", encoding = "utf-8") as csvfile:
                    fieldnames = ["destination", "airport_initials", "flight_time", "distance_from_iceland", "contact_name", "emergency_phone_nr"]
                    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
                    writer.writeheader()
                    
                    for destination in destinations:
                        writer.writerow({"destination": destination.destination, "airport_initals": destination.airport_initials, "flight_time": destination.flight_time, "distance_from_iceland": destination.ditance_from_iceland, "contact_name": destination.contact_name, "emergency_phone_nr": destination.emergency_phone_nr})
