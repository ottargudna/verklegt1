import csv
from Model.voyage import Voyage

class Voyage_Data:
    def __init__(self) -> None:
        self.file_name = "Files/voyage.csv"


    def get_all_voyages(self):
        list = []
        with open(self.file_name, newline= '', encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list.append(Voyage(row["voyage_number"],row ["dep_from"], row ["arr_at"], row ["aircraft_id"], row ["date_out"], row ["date_home"], row ["captain"], row ["copilot"], row ["flight_service_manager"], row ["flight_attendant1"], row ["flight_attendant2"]))
        return list 
    

    def create_voyage(self, voyage):
        with open(self.file_name, 'a', newline= '', encoding = "utf-8") as csvfile:
            fieldnames = ["voyage_number", "dep_from", "arr_at", "aircraft_id", "date_out", "date_home", "captain", "copilot", "flight_service_manager", "flight_attendant1", "flight_attendant2"]
            writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
            writer.writerow({"voyage_number": voyage.voyage_number,"dep_from": voyage.dep_from, "arr_at": voyage.arr_at, "aircraft_id": voyage.aircraft_id, "date_out": voyage.date_out, "date_home": voyage.date_home, "captain": voyage.captain, "copilot": voyage.copilot, "flight_service_manager": voyage.flight_service_manager, "flight_attendant1": voyage.flight_attendant1, "flight_attendant2": voyage.flight_attendant2})


    def update_voyages(self, updated_voyage):
        voyages = self.get_all_voyages() 

        for voyage in voyages: 
            if voyage.voyage_number == updated_voyage.voyage_number:
                #update the voyage crew information

                voyage.captain = updated_voyage.captain
                voyage.copilot = updated_voyage.copilot
                voyage.flight_service_manager = updated_voyage.flight_service_manager
                voyage.flight_attendant1 = updated_voyage.flight_attendant1
                voyage.flight_attendant2 = updated_voyage.flight_attendant2

                with open(self.file_name, "w+", newline = '', encoding = "utf-8") as csvfile:
                    fieldnames = ["voyage_number", "dep_from", "arr_at", "aircraft_id", "date_out", "date_home", "captain", "copilot", "flight_service_manager", "flight_attendant1", "flight_attendant2"]
                    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
                    writer.writeheader()
                    
                    for voyage in voyages:
                        writer.writerow({"voyage_number": voyage.voyage_number, "dep_from": voyage.dep_from, "arr_at": voyage.arr_at, "aircraft_id": voyage.aircraft_id, "date_out": voyage.date_out, "date_home": voyage.date_home, "captain": voyage.captain, "copilot": voyage.copilot, "flight_service_manager": voyage.flight_service_manager, "flight_attendant1": voyage.flight_attendant1, "flight_attendant2": voyage.flight_attendant2})

