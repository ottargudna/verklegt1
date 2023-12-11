import csv
from Model.airplane import Airplane

class Airplane_Data:
    def __init__(self) -> None:
        self.file_name = "Files/airplane.csv"


    def get_all_airplanes(self):
        list = []
        with open(self.file_name, newline= '', encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list.append(Airplane(row["name"], row ["plane_type"], row ["manufacturer"], row ["number_of_passanger_seats"]))
        return list 
    
    def create_airplane(self, Airplane):
        with open(self.file_name, "a", newline= " ", encoding = " utf-8") as csvfile:
            fieldnames = ["name","plane_type","manufacturer", "number_of_passanger_seats"]
            writer = csv.DictReader(csvfile,fieldnames = fieldnames) 