import csv
from Model.employee import Employee

class Employee_Data:
    def __init__(self) -> None:
        self.file_name = "Files/crew.csv"

    def get_all_employees(self):
        list = []
        with open(self.file_name, newline= '', encoding = "utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list.append(Employee(row["nid"], row ["name"], row ["role"], row ["rank"], row ["address"], row ["phone_nr"]))
        return list 
    
    def create_employee(self, employee):
        with open(self.file_name, "a", newline= " ", encoding = " utf-8") as csvfile:
            fieldnames = ["nid","name","role", "rank", "address", "phone_nr"]
            writer = csv.DictReader(csvfile,fieldnames = fieldnames) 


        
