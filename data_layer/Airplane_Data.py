import csv
from Model.airplane import Airplane

class Airplane_Data:
    def __init__(self) -> None:
        self.file_name = "Files/aircraft.csv"


    def get_all_airplanes(self):
        list = []
        with open(self.file_name, newline= '', encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list.append(Airplane(row["plane_insignia"], row ["plane_type_id"], row ["capacity"]))
        return list 
    
<<<<<<< Updated upstream
    def create_airplane(self, Airplane):
        with open(self.file_name, "a", newline= " ", encoding = " utf-8") as csvfile:
            fieldnames = ["plane_insignia","plane_type_id","capacity"]
            writer = csv.DictReader(csvfile,fieldnames = fieldnames) 
            writer.writerow({"plane_insignia": Airplane.plane_insignia, "plane_type_id": Airplane.plane_type_id, "capacity": Airplane.capacity})
=======
    def create_airplane(self, airplane):
        with open(self.file_name, "a", newline= '', encoding = "utf-8") as csvfile:
            fieldnames = ["plane_insignia","plane_type_id","capacity"]
            writer = csv.DictWriter(csvfile,fieldnames = fieldnames) 
            writer.writerow({"plane_insignia": airplane.plane_insignia, "plane_type_id": airplane.plane_type_id, "capacity": airplane.capacity})
>>>>>>> Stashed changes
