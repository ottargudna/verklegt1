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
                list.append(Voyage(row["destination"], row ["airport"], row ["captain"], row ["copilot"], row ["flight_attendant"], row ["date"]))
        return list 
    
    def create_voyage(self, Voyage):
        with open(self.file_name, "a", newline= " ", encoding = " utf-8") as csvfile:
            fieldnames = ["destination","airport", "captain", "copilot", "flight_attendant", "date"]
            writer = csv.DictReader(csvfile,fieldnames = fieldnames)