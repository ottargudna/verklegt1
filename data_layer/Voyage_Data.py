import csv
from Model.voyage import Voyage

class Voyage_Data:
    def __init__(self) -> None:
        self.file_name = "File/voyage.csv"


    def get_all_voyages(self):
        list = []
        with open(self.file_name, newline= '', encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list.append(Voyage(row["dep_from"], row ["arr_at"], row ["aircraft_id"], row ["date_out"], row ["date_home"], row ["captain"], row ["copilot"], row ["flight_service_manager"], row ["flight_attendant1"], row ["flight attendant2"]))
        return list 
    
    def create_voyage(self, Voyage):
        with open(self.file_name, "a", newline= " ", encoding = " utf-8") as csvfile:
            fieldnames = ["dep_from", "arr_at", "aircraft_id", "date_out", "date_home", "captain", "copilot", "flight_service_manager", "flight_attendant1", "flight_attendant2"]
            writer = csv.DictReader(csvfile,fieldnames = fieldnames)
            writer.writerow({"dep_from": Voyage.dep_from, "arr_at": Voyage.arr_at, "aircraft_id": Voyage.aircraft_id, "date_out": Voyage.date_out, "date_home": Voyage.date_home, "captain": Voyage.captain, "copilot": Voyage.copilot, "flight_service_manager": Voyage.flight_sevice_manager, "flight_attendant1": Voyage.flight_attendant1, "flight_attendant2": Voyage.flight_attendant2})